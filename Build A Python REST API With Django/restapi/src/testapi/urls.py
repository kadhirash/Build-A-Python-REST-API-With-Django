"""testapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from updates.views import (
    json_example_view,
    JsonCBV,
    JsonCBV2,
    SerializedListView,
    SerializedDetailView,
)

urlpatterns = [
    path("", json_example_view),
    path("admin/", admin.site.urls),
    path(
        "api/updates/", include("updates.api.urls")
    ),  # api/updates/ --> api/updates/1/ --> detail
    # path("json/example/", json_example_view),
    # # Json Class Based View
    # path("json/cbv/", JsonCBV.as_view()),
    # path("json/cbv2/", JsonCBV2.as_view()),
    # # Serialize
    # path("json/serialized/list/", SerializedListView.as_view()),
    # path("json/serialized/detail/", SerializedDetailView.as_view()),
]
