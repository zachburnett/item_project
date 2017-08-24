from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^add_item$', views.add_item),
    # url(r'^remove/(?P<item_id>\d+)/(?P<user_id>\d+)$',views.remove),
    url(r'^add_to/(?P<item_id>\d+)/(?P<user_id>\d+)$',views.add_to),
    url(r'^delete%', views.delete),
    url(r'^show/(?P<item>\d+)$', views.show)
]