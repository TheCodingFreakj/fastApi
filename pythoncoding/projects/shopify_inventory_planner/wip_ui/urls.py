from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings

from wip_ui.views import serve_react

urlpatterns = [
    path("", serve_react, {"document_root": settings.REACT_APP_BUILD_PATH}),
]