from django.shortcuts import render
from MX3.models import Publishert, Gamestudiot, Gametitlet, Gamert, Buyt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime


def publishers_list(request):
	publishers = Publishert.objects.all()
	return render(request, 'publishers_list.html', {'publishers': publishers, 'user': request.user})

def publisher_info(request, pid):
	pub = Publishert.objects.get(pid=pid)
	pub_studio = Gamestudiot.objects.all().filter(pid=pid)
        pub_games = Gametitlet.objects.all().filter(pid=pid)
	return render(request, 'publisher_info.html', {'publisher': pub,
            'publisher_studio': pub_studio, 'publisher_games': pub_games, 'user': request.user})

def game_info(request, gtid):
    gametitle = Gametitlet.objects.all().get(gtid=gtid)

    if request.method == "POST":
        gamer = Gamert.objects.all().get(username= request.user.username)
        if gamer.user_account_balance < gametitle.price:
            return HttpResponse('your balance is not enough! <br/> <a href="/game/%s"> back to game page </a>'%gametitle.gtid)
        gamer.user_account_balance -= gametitle.price
        gamer.save()
        buy = Buyt(gid=gamer, gtid=gametitle, date=datetime.now())
        buy.save()
        return HttpResponse('you bought this game!  <br/> <a href="/game/%s"> back to game page </a>'%gametitle.gtid)

    own_this_game = False
    if request.user.is_authenticated:
    	gid = Gamert.objects.all().get(username= request.user.username).gid
    	if Buyt.objects.all().filter(gid = gid, gtid = gtid).count() > 0:
            own_this_game = True
    return render(request, 'game_info.html', {'game': gametitle, 'user': request.user, 'own_this_game' : own_this_game})

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
        return render(request, 'gamer_login.html', {'user': request.user})

def gamer_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        phone_number = request.POST["phone"]
        name = request.POST["name"]
        check_unique1 = Gamert.objects.all().filter(username = username)
        check_unique2 = Gamert.objects.all().filter(username = username)
        check_unique3 = Gamert.objects.all().filter(username = username)

        if check_unique1.count() > 0 or check_unique2.count() > 0 or check_unique3.count() > 0 or len(password) < 8:
            return HttpResponse('Invalid! <br/> <a href="/login"> try again </a>')

        django_user = User(username=username, password=password, email=email)
        django_user.set_password(password)
        django_user.save()
        gamer_gid = Gamert.objects.all().count() + 1
        gamer = Gamert(gid=gamer_gid, name=name, username=username, password=password, email=email,
                phone_number=phone_number, django_user=django_user, user_account_balance=0)
        gamer.save()
        login(request, django_user)
        return HttpResponseRedirect('/gamer/%s'%(django_user.username))
    else:
        return render(request, 'signup.html', {'user': request.user})

def gamer_profile(request,username):
    gamer = Gamert.objects.all().get(username = username)
    return render(request, 'gamer_profile.html', {'gamer': gamer, 'username': username, 'user': request.user})

def notfound(request):
    return render(request, '404.html', {'user': request.user})

def index(request):
    games = Gametitlet.objects.all()
    publishers = Publishert.objects.all()
    gamers = Gamert.objects.all()
    return render(request, 'index.html', {'games': games, 'publishers': publishers, 'user': request.user, 'user': request.user,
        'gamers': gamers})

def gamer_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
