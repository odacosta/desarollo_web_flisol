from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app_ejemplo/', include('app_ejemplo.urls', namespace='app_ejemplo')),
]
