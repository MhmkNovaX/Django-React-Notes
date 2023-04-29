from django.urls import path, include


urlpatterns = [
    path('api/', include('note.views.api.urls')),
]
