from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, register

app_name = 'api'

urlpatterns = {
    url(r'^user/', register, name='user'),
    url(r'^admin/', CreateView.as_view(), name="admin"),
    url(r'^admin/(?P<pk>[0-9]+)', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
