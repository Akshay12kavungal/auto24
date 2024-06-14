from django.urls import path,include

from rest_framework.routers import DefaultRouter

from customer_management.api.views import CustomerSerializerViewset, FeedbackSerializerViewset, NotificationSerializerViewset, ServiceRequestSerializerViewset, VehicleSerializerViewset


router=DefaultRouter()

router.register(r'customer',CustomerSerializerViewset)
router.register(r'vehicle',VehicleSerializerViewset)
router.register(r'service-request',ServiceRequestSerializerViewset)
router.register(r'feedback',FeedbackSerializerViewset)
router.register(r'notification',NotificationSerializerViewset)


urlpatterns=[
    path('',include(router.urls))
]


