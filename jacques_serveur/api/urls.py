from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from api.views.bucketlist import BucketlistView, BucketlistDetailView
from api.views.user import UserView, UserDetailView
from api.views.offer import OfferView, OfferDetailView, OfferExpandView#, DegreeDetailView, SkillDetailView, LanguageDetailView, ContractDetailView, LocationDetailView, CompanyDetailView

urlpatterns = {
    url(r'^users/$', UserView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
    url(r'^bucketlists/$', BucketlistView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailView.as_view()),
    url(r'^offers/$', OfferView.as_view()),
    url(r'^offers/(?P<pk>[0-9]+)/$', OfferDetailView.as_view()),
    url(r'^offers/(?P<pk>[0-9]+)/expand/$', OfferExpandView.as_view())#,
    # url(r'^degree/(?P<pk>[0-9]+)/$', DegreeDetailView.as_view()),
    # url(r'^skill/(?P<pk>[0-9]+)/$', SkillDetailView.as_view()),
    # url(r'^language/(?P<pk>[0-9]+)/$', LanguageDetailView.as_view()),
    # url(r'^contract/(?P<pk>[0-9]+)/$', ContractDetailView.as_view()),
    # url(r'^location/(?P<pk>[0-9]+)/$', LocationDetailView.as_view()),
    # url(r'^company/(?P<pk>[0-9]+)/$', CompanyDetailView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
