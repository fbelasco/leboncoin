from django.conf.urls import url, include
from django.contrib import admin
from .api import router

# interface pour admin et api (CRUD)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
