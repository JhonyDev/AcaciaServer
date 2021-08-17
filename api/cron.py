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


def run_cron_view(request):
    # run_cron()
    return HttpResponse("finished")
