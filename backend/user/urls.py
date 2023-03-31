from django.urls import path
from .views import UserListAndCreate, UserCreateAnonymous, UserEditAdmin, UserEditLoggedIn

urlpatterns = [
    # APIs
    path("api/", UserCreateAnonymous.as_view(), name="UserCreateAnonymous"),
    path("api/me/", UserEditLoggedIn.as_view(), name="UserEditLoggedIn"),
    # Admins
    path("admin/", UserListAndCreate.as_view(), name="UserListAndCreate"),
    path("admin/<int:pk>/", UserEditAdmin.as_view(), name="UserEditAdmin"),
]
