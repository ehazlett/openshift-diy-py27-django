import platform
from django.http import HttpResponse
import os

def system_info(request):
    python_version = platform.python_version()
    return HttpResponse('Running {0} on Python version {1}'.format(os.environ.get('OPENSHIFT_APP_NAME', 'app'), python_version), content_type='text/plain')
