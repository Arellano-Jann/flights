from django.contrib import admin
from .models import Agent, Protocol, Endpoint, Task, TaskResult, Credential, File, Log

# Register your models here.
admin.site.register(Agent)
admin.site.register(Protocol)
admin.site.register(Endpoint)
admin.site.register(Task)
admin.site.register(TaskResult)
admin.site.register(Credential)
admin.site.register(File)
admin.site.register(Log)