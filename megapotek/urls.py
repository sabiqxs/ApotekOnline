from django.conf.urls import url
from . import views
from . views import \
    dataobat_list, dataobat_create, \
    dataobat_delete, dataobat_detail, \
    dataobat_update

urlpatterns = [
    # url(r'^/$', views.index, name='index'),
    url(r'^/$', dataobat_list, name='index'),

    url(r'^/dataobat/', dataobat_list),
    url(r'^create/', dataobat_create),
    url(r'^update/', dataobat_update),
    url(r'^delete/', dataobat_delete),
    url(r'^/(?P<id>\d+)/$', dataobat_detail, name='detail'),

    url(r'^contact/', views.index, name='contact'),
    url(r'^register_login/$', views.registerLogin, name='register_login'),
]