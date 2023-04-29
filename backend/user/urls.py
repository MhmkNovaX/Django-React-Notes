from django.urls import include, path

urlpatterns = [
    path('api/', include('user.views.api.urls')),
]
