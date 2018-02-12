from django.conf.urls import url
from games.views import game_list, game_detail

urlpatterns = [
    url(r'^$', game_list, name='game_list'),
    url(r'^/(?P<pk>[0-9]+)/$', game_detail, name='game_detail'),
]