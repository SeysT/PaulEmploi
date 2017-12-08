from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from api.views.bucketlist import BucketlistView, BucketlistDetailView
from api.views.user import UserView, UserDetailView


urlpatterns = {
    url(r'^users/$', UserView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
    url(r'^bucketlists/$', BucketlistView.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
