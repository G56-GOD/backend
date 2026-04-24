from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    TransactionViewSet,AuthenticationViewsets, TransferView,
    MyNotification
)

router = DefaultRouter()
router.register(r'auth',AuthenticationViewsets,'auth')
router.register(r'transactions',TransactionViewSet,'transactions')

urlpatterns = [
    path('api/', include(router.urls)),
    path('transfers/', Transfer.as_view(), name='transfers'),
    path('notifications/', MyNotification.as_view(), name='notifications')
]