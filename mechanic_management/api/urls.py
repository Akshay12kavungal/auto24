from django.urls import path,include
from rest_framework.routers import DefaultRouter

from mechanic_management.api.views import MechanicEarningsSerializerViewset, MechanicSerializerViewset, MechanicWorkSerializerViewset

router=DefaultRouter()

router.register(r'mechanic',MechanicSerializerViewset)
router.register(r'mechanic_work',MechanicWorkSerializerViewset)
router.register(r'mechanic_earnings',MechanicEarningsSerializerViewset)


urlpatterns=[
    path('',include(router.urls))
]