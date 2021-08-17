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
    users = User.objects.all()
    for user in users:

        if user.paid_fee:
            list_paid_user = PaidUsers.objects.filter(user_name=user.name, user_email=user.user_email)
            if list_paid_user:
                continue
            new_paid_user = PaidUsers()
            new_paid_user.user_email = user.user_email
            new_paid_user.user_name = user.name
            new_paid_user.user_image = user.profile_image
            new_paid_user.save()
        else:
            list_un_paid_user = UnPaidUsers.objects.filter(user_name=user.name, user_email=user.user_email)
            if list_un_paid_user:
                continue
            new_un_paid_user = UnPaidUsers()
            new_un_paid_user.user_email = user.user_email
            new_un_paid_user.user_name = user.name
            new_un_paid_user.user_image = user.profile_image
            new_un_paid_user.save()

    list_paid_user = User.objects.all()
    for user in list_paid_user:
        new_list_paid_user = PaidUsers.objects.filter(user_name=user.name, user_email=user.user_email)

        if not new_list_paid_user:
            continue

        if user.paid_fee:
            continue

        user.paid_fee = True
        user.save()


def run_cron_view(request):
    run_cron()
    return HttpResponse("finished")
