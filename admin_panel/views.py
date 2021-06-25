import threading
import time

from django.http import JsonResponse
from django.views.generic import View, TemplateView

from .models import AdminCred


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

        return JsonResponse({'data': creds}, safe=False)


def expire(x, creds):
    print('thread running')
    time.sleep(5 * 60)
    print('thread ended should expire session')
    temp = AdminCred.objects.get(pk=creds.get('id'))
    temp.status = 0
    temp.save()
