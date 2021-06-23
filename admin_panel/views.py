from django.http import HttpResponse
from django.template import loader


def load(request):
    template = loader.get_template('admin_panel/CustomerSupport.html')
    abc = {}
    return HttpResponse(template.render(abc, request))
