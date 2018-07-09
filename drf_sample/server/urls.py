from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from retail.views import ChainViewSet, StoreViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(prefix='chains', viewset=ChainViewSet)
router.register(prefix='stores', viewset=StoreViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)

urlpatterns = router.urls
