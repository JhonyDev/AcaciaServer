from django.http import HttpResponse

from .models import User
from admin_panel.models import PaidUsers, UnPaidUsers


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

        print("Adding to paid users")

        paid_user.paid_fee = True
        paid_user.save()

    print("Cron Ended")


def run_cron_view(request):
    run_cron()
    return HttpResponse("finished")
