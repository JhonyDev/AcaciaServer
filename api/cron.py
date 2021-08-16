from django.http import HttpResponse

from .models import User
from admin_panel.models import PaidUsers, UnPaidUsers

from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth

cred = credentials.Certificate("/home/adminuser/AcaciaServer/mate-1d51c-firebase-adminsdk-r3icd-f455e2461f.json")
firebase_admin.initialize_app(cred)


def init_firebase(request):
    page = auth.list_users()
    a_list = None
    for user in page.users:
        a_list.append(str(user.uid))

    result = auth.delete_users(a_list)

    print('Successfully deleted {0} users'.format(result.success_count))
    print('Failed to delete {0} users'.format(result.failure_count))
    for _ in result.errors:
        print('error #{0}, reason: {1}'.format(result.index, result.reason))

    return HttpResponse("finished")


def run_cron():
    print('Cron running')
    paid_users = User.objects.filter(paid_fee=True)
    for paid_user in paid_users:
        print('paid user = ', paid_user.user_id)
        list_paid_user = PaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if list_paid_user:
            continue
        print('Adding to paid users : ', paid_user.user_id)
        new_paid_user = PaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

        list_un_paid_user = UnPaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)
        for un_paid_user in list_un_paid_user:
            un_paid_user.delete()

    paid_users = User.objects.filter(paid_fee=False)
    for paid_user in paid_users:
        print('Unpaid User : ', paid_user.user_id)

        list_paid_user = UnPaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if list_paid_user:
            continue

        print('Adding to Unpaid User : ', paid_user.user_id)

        new_paid_user = UnPaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

    list_paid_user = User.objects.all()

    for paid_user in list_paid_user:
        new_list_paid_user = PaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        print("Check if user exists in paid")

        if not new_list_paid_user:
            continue

        if paid_user.paid_fee:
            print('Already paid enabled')
            continue

        print()
        print("Adding to paid users = ", paid_user.name)

        paid_user.paid_fee = True
        paid_user.save()

    print("Cron Ended")


def run_cron_view(request):
    run_cron()
    return HttpResponse("finished")
