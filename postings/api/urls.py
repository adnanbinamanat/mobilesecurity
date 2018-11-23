from django.conf.urls import url


from .views import ApiPostRudView, ApiPostAPIView

urlpatterns = [
    url(r'^$', ApiPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', ApiPostRudView.as_view(), name='post-rud'),
]
