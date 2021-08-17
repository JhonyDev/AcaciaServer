import threading
import time

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView

from .models import *
from api.models import *


# def load(request):
#     admin_creds = AdminCred.objects.all()
#     creds = None
#     for admin_cred in admin_creds:
#         creds = admin_cred
#
#     template = loader.get_template('admin_panel/AdminPanel.html')
#     login_data = {'data': creds}
#     return HttpResponse(template.render(login_data, request))


class MainView(TemplateView):
    template_name = 'admin_panel/Login.html'


class PassView(TemplateView):
    template_name = 'admin_panel/Password.html'


class DashboardView(TemplateView):
    template_name = 'admin_panel/AdminPanel.html'


class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print('KWARGS ' + str(kwargs))

        admin_creds = list(AdminCred.objects.values())
        creds = None
        for admin_cred in admin_creds:
            creds = admin_cred
        if kwargs['result'] == 1:
            print('updating status')
            print(creds)
            thread = threading.Thread(target=expire, args=('1', creds))
            thread.start()
            temp = AdminCred.objects.get(pk=creds.get('id'))
            temp.status = 1
            temp.save()

        return JsonResponse({'data': creds}, safe=False)


class AdminJson(View):
    def get(self, *args, **kwargs):
        print('this is admin js ' + str(kwargs))
        print(kwargs)
        admin_creds = list(AdminCred.objects.values())
        creds = None
        for admin_cred in admin_creds:
            creds = admin_cred

        reported_accounts = list(ReportedAccounts.objects.values())

        users = list(User.objects.values())

        paid_users = []
        unpaid_users = []
        for user in users:
            if user.paid_fee:
                paid_user = PaidUsers()
                paid_user.user_image = user.profile_image
                paid_user.user_email = user.user_email
                paid_user.user_name = user.name
                paid_users.append(paid_users)
            else:
                unpaid = UnPaidUsers()
                unpaid.user_image = user.profile_image
                unpaid.user_email = user.user_email
                unpaid.user_name = user.name
                unpaid_users.append(unpaid)

        verified_users = []
        unverified_users = []

        for user in users:
            if user.get('verification_status') == 'Verified':
                verified_users.append(user)
            else:
                unverified_users.append(user)

        users = list(User.objects.all())

        print('paid_users')
        print(paid_users)

        return JsonResponse(
            {'data': creds,
             'report': reported_accounts,
             'paid_users': paid_users,
             'unpaid_users': unpaid_users,
             'verified_users': verified_users,
             'unverified_users': unverified_users,
             'total_users': len(users), }
            , safe=False)


class PassJson(View):
    def get(self, *args, **kwargs):
        json_admin = None
        admin_cred = list(AdminCred.objects.values())
        for admin in admin_cred:
            json_admin = admin
            break
        return JsonResponse(
            {'data': json_admin}
            , safe=False)


class ButtonClick(View):
    def get(self, *args, **kwargs):
        print(kwargs)

        reported_account = ReportedAccounts.objects.filter(user_email=kwargs.get('result'))
        for account in reported_account:
            account.delete()

        return HttpResponseRedirect('/admin_panel/dashboard/')


class NewPass(View):
    def get(self, *args, **kwargs):
        new_password = kwargs.get('result')
        admin_cred = AdminCred.objects.get(user_name='admin')
        admin_cred.password = new_password
        admin_cred.save()
        return HttpResponseRedirect('/admin_panel/dashboard/password/')


def expire(x, creds):
    print('thread running')
    time.sleep(5 * 60)
    print('thread ended should expire session')
    temp = AdminCred.objects.get(pk=creds.get('id'))
    temp.status = 0
    temp.save()
