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
    a_list = []
    for user in page.users:
        a_list.append(str(user.uid))

    result = auth.delete_users(a_list)

    print('Successfully deleted {0} users'.format(result.success_count))
    print('Failed to delete {0} users'.format(result.failure_count))
    for _ in result.errors:
        print('error #{0}, reason: {1}'.format(result.index, result.reason))

    return HttpResponse("finished")


def run_cron():
    paid_users = User.objects.filter(paid_fee=True)
    for paid_user in paid_users:
        list_paid_user = PaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if list_paid_user:
            continue
        new_paid_user = PaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

    paid_users = User.objects.filter(paid_fee=False)
    for paid_user in paid_users:
        list_paid_user = UnPaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if list_paid_user:
            continue

        new_paid_user = UnPaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

    list_paid_user = User.objects.all()

    for paid_user in list_paid_user:
        new_list_paid_user = PaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if not new_list_paid_user:
            continue

        if paid_user.paid_fee:
            continue

        paid_user.paid_fee = True
        paid_user.save()

    list_paid_user = PaidUsers.objects.all()
    for paid in list_paid_user:
        list_un_paid = UnPaidUsers.objects.filter(user_name=paid.user_name, user_email=paid.user_email)
        for unpaid in list_un_paid:
            unpaid.delete()


def run_cron_view(request):
    run_cron()
    return HttpResponse("finished")
