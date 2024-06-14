from django.urls import include, path

from rest_framework.routers import DefaultRouter

from admin_management.api.views import AdminCommissionSerializerViewset

router = DefaultRouter()
router.register(r'AdminCommission', AdminCommissionSerializerViewset)

urlpatterns=[
    path('',include(router.urls))
]