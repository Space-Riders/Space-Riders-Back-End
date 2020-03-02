from django.conf.urls import url
from . import api

urlpatterns = [
    url('boost', api.boost),
    url('teleport', api.teleport),
    url('leaderboard', api.leaderboard),
    url('battle', api.battleResults),
    url('matrix', api.getMatrix),
    url('coors', api.getRoomCoors),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]