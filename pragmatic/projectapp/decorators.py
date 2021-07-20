from projectapp.models import Project
from django.http import HttpResponseForbidden

def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        if not project.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated