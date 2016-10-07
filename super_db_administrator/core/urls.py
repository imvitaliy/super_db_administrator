
from django.conf.urls import url, include
from django.contrib import admin

from .views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^$', IndexView.as_view())
]
