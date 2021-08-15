from .models import User
from admin_panel.models import PaidUsers, UnPaidUsers


def run_cron():
    paid_users = User.objects.filter(paid_fee=True)
    for paid_user in paid_users:
        paid_user = PaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if not paid_user:
            continue

        new_paid_user = PaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

    paid_users = User.objects.filter(paid_fee=False)
    for paid_user in paid_users:
        paid_user = UnPaidUsers.objects.filter(user_name=paid_user.name, user_email=paid_user.user_email)

        if not paid_user:
            continue


        new_paid_user = UnPaidUsers()
        new_paid_user.user_email = paid_user.user_email
        new_paid_user.user_name = paid_user.name
        new_paid_user.user_image = paid_user.profile_image
        new_paid_user.save()

    list_paid_user = PaidUsers.objects.all()

    for paid_user in list_paid_user:
        paid_user = User.objects.filter(name=paid_user.user_name, user_email=paid_user.user_email)

        if not paid_user:
            continue

        paid_user.paid_fee = True
        paid_user.save()
