from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UsersView

router = DefaultRouter()
router.register('users', UsersView, basename='users')
urlpatterns = [
    path('', include(router.urls))
]