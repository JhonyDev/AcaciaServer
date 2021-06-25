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


class PostJsonListView(View):
    def get(self, *args, **kwargs):
        admin_creds = list(AdminCred.objects.values())
        creds = None
        for admin_cred in admin_creds:
            creds = admin_cred

        return JsonResponse({'data': creds}, safe=False)
