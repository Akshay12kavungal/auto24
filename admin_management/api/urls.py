from django.urls import include, path

from rest_framework.routers import DefaultRouter

from admin_management.api.views import AdminCommissionSerializerViewset, CustomersSerializerViewSet, MechanicsSerializerViewSet

router = DefaultRouter()
router.register(r'adminCommission', AdminCommissionSerializerViewset)
router.register(r'customers', CustomersSerializerViewSet)
router.register(r'mechanics', MechanicsSerializerViewSet)

urlpatterns=[
    path('',include(router.urls))
]