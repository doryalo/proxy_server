from django.contrib.admin import AdminSite
from django_celery_results.admin import TaskResultAdmin, TaskResult


class CyeAdmin(AdminSite):
    pass


admin = CyeAdmin('admin_panel')
admin.register(TaskResult, TaskResultAdmin)
