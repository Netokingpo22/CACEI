from django.urls import include, path

urlpatterns = [
    path('api/v1/', include("Usuario.urls")),
    path('api/v1/', include("Maestro.urls")),
]
