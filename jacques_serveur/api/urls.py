from rest_framework.routers import DefaultRouter

from api.views.fields import FieldsViewSet
from api.views.offer import OfferViewSet
from api.views.profile import ProfileViewSet


router = DefaultRouter()
router.register(r'offers', OfferViewSet, base_name='offer')
router.register(r'profile', ProfileViewSet, base_name='profile')
router.register(r'fields', FieldsViewSet, base_name='field')

urlpatterns = router.urls
