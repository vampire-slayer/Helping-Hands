from django.shortcuts import render
from django.http import HttpResponse
from . models import Community, Members

# Create your views here.
def index(request):
	all_community = Community.objects.all()
	# html = ''
	# for community in all_community:
	# 	url = '/community/' + str(community.id) + '/'
	# 	html += '<a href ="' + url + '">' + community.name + '</a><br>'

	# return HttpResponse(html)
	context = {'all_community' : all_community}
	return render(request, 'community/index.html', context)

def detail(request, community_id):
	return HttpResponse("<h2> Details of Community " + str(community_id) + "</h2>")
