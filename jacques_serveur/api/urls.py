from rest_framework.routers import DefaultRouter

from api.views.offer import OfferViewSet
from api.views.user import UserViewSet

router = DefaultRouter()
router.register(r'offers', OfferViewSet, base_name='offer')
router.register(r'users', UserViewSet, base_name='user')

# urlpatterns = {
#     url(r'^users/$', UserView.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
#     url(r'^bucketlists/$', BucketlistView.as_view()),
#     url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailView.as_view()),
#     url(r'^offers/$', OfferView.as_view()),
#     url(r'^offers/(?P<pk>[0-9]+)/$', OfferDetailView.as_view()),
#     url(r'^offers/(?P<pk>[0-9]+)/expand/$', OfferExpandView.as_view()),
#     # url(r'^degree/(?P<pk>[0-9]+)/$', DegreeDetailView.as_view()),
#     # url(r'^skill/(?P<pk>[0-9]+)/$', SkillDetailView.as_view()),
#     # url(r'^language/(?P<pk>[0-9]+)/$', LanguageDetailView.as_view()),
#     # url(r'^contract/(?P<pk>[0-9]+)/$', ContractDetailView.as_view()),
#     # url(r'^location/(?P<pk>[0-9]+)/$', LocationDetailView.as_view()),
#     # url(r'^company/(?P<pk>[0-9]+)/$', CompanyDetailView.as_view()),
# }

urlpatterns = router.urls
