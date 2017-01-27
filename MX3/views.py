from django.shortcuts import render
from MX3.models import Publishert, Gamestudiot, Gametitlet, Gamert  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


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
    return render(request, 'game_info.html', {'game': gametitle})

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

        if check_unique1.count() > 0 or check_unique2.count() > 0 or check_unique3.count() > 0:
            return HttpResponse('Invalid! <br/> <a href="/login"> try again </a>')
        
        django_user = User(username = username, password = password)
        django_user.save() 
        user_account_balance = 0
        gamer_gid = Gamert.objects.all().count() + 1 
        gamer = Gamert(gamer_gid, username = username, password = password, email = email,
                phone_number = phone_number, django_user = django_user, user_account_balance = 0)
        gamer.save()
        login(request, django_user)
        return HttpResponseRedirect('/gamer/%s'%(django_user.username))
    else:
        return render(request, 'signup.html')

def gamer_profile(request,username):
    gamer = Gamert.objects.all().get(username = username)
    return render(request, 'gamer_profile.html', {'gamer': gamer, 'username': username})
   
def notfound(request):
    return render(request, '404.html')

def index(request):
    games = Gametitlet.objects.all()
    publishers = Publishert.objects.all()
    return render(request, 'index.html', {'games': games, 'publishers': publishers})

