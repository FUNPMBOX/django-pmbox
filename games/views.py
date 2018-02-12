from django.shortcuts import render
from django.conf import settings
from games.models import Game

# Create your views here.


def home(request):
    data = {}
    data['brand'] = settings.BRAND
    data['social_media'] = settings.SOCIAL_MEDIA
    return render(request, 'games/home.html', data)

def game_list(request):
    games = Game.objects.all()
    data = {}
    data['games'] = games
    data['brand'] = settings.BRAND
    data['social_media'] = settings.SOCIAL_MEDIA
    print(data)
    return render(request, 'games/game_list.html', data)

def game_detail(request, pk):
    data = {}
    game = Game.objects.get(pk=pk)
    data['game'] = game
    data['materials'] = game.material.all()
    data['brand'] = settings.BRAND
    data['social_media'] = settings.SOCIAL_MEDIA
    return render(request, 'games/game_detail.html', data)


