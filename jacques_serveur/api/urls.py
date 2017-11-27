from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.bucketlist_views import BucketlistView, BucketlistDetailView


urlpatterns = {
    url(r'^bucketlists/$', BucketlistView.as_view(), name='create'),
    url(
        r'^bucketlists/(?P<pk>[0-9]+)/$',
        BucketlistDetailView.as_view(),
        name="details"
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
