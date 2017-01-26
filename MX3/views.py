from django.shortcuts import render
from MX3.models import Publishert, Gamestudiot

def publishers_list(request):
	publishers = Publishert.objects.all()
	return render(request, 'publishers_list.html', {'publishers': publishers})

def publisher_info(request, pid):
	pub = Publishert.objects.get(pid=pid)
	pub_studio = Gamestudiot.objects.all().filter(pid=pid)
	return render(request, 'publisher_info.html', {'publisher': pub,
			'publisher_studio': pub_studio})
