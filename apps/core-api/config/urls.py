from django.contrib import admin
from django.urls import include, path


admin.site.site_header = "مدیریت سامانه MGSM"
admin.site.site_title = "پنل مدیریت MGSM"
admin.site.index_title = "مدیریت بات فروش"


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/v1/",
        include("apps.common.urls"),
    ),
]
