from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    if request.user.is_authenticated:
        return HttpResponse(
            f"<h1>Hello, {request.user.email}</h1>"
            '<a href="/accounts/logout/">Sign out</a>'
        )
    return HttpResponse(
        "<h1>OttoSpace + django-allauth</h1>"
        '<a href="/accounts/oidc/ottospace/login/">Sign in with OttoSpace</a>'
    )


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
