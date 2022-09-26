from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = "my_name"
router = SimpleRouter()
router.register("accounts", views.AccountViewSet)
router.register("user", views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))

]
