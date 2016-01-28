from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

def HomePage(request):
	context = {}
	return render_to_response('homepage.html', context, context_instance=RequestContext(request))