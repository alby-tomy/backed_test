from django.urls import path, include
from .views import feedback_view, success_view, admin_dashboard, login


app_name = "demo"

urlpatterns = [
    path('', view=feedback_view, name='demo_name'),
    path('success/', view=success_view, name='success'),
    path('login/', view=login, name='login'),
    path('admin_dashboard/', view=admin_dashboard, name='admin_dashboard'),
]
