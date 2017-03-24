from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from crash.forms import CrashForm


@method_decorator(csrf_exempt, name='dispatch')
class CrashSubmitView(View):
    def post(self, request):
        crash_form = CrashForm(self.request.POST)
        if crash_form.is_valid():
            crash_form.save()
            saved = True
        else:
            saved = False
        return JsonResponse({
            'saved': saved,
        })
