from django.shortcuts import render
from MX3.models import Publishert, Gamestudiot, Gametitlet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def publishers_list(request):
	publishers = Publishert.objects.all()
	return render(request, 'publishers_list.html', {'publishers': publishers})

def publisher_info(request, pid):
	pub = Publishert.objects.get(pid=pid)
	pub_studio = Gamestudiot.objects.all().filter(pid=pid)
        pub_games = Gametitlet.objects.all().filter(pid=pid)
	return render(request, 'publisher_info.html', {'publisher': pub,
            'publisher_studio': pub_studio, 'publisher_games': pub_games})

def game_info(request, gtid):
    gametitle = Gametitlet.objects.all().filter(gtid=gtid)
    return render(request, 'game_info.html', {'gametitle': gametitle})

def gamer_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return HttpResponseRedirect('/gamer/%s'%(user.username))
        else:
            return HttpResponse('Invalid username or password! <br/> <a href="/login"> try again </a>')
    else:
        return render(request, 'gamer_login.html')

def gamer_profile(request):
    pass
