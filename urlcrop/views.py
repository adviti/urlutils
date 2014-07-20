# Create your views here.

import  urlcrop.utils as urlcrop_utils
from urlcrop.models import Url

from django.utils import html
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    context = {}
    if request.method == 'GET':
        return render_to_response('urlcrop/home.html', context, context_instance=RequestContext(request))
    else:
        url = Url()

        actual_url = request.POST.get('url')
        unquoted_actual_url = html.unquote(actual_url)
        url.actual_url = unquoted_actual_url

        url.save()

        url_id = url.id
        url_hash = urlcrop_utils.get_unique_hash(str(url_id))
        url.url_hash = url_hash

        short_url = urlcrop_utils.get_actual_short_url(url_hash)
        url.save()

        context.update({'short_url': short_url})

        return render_to_response("urlcrop/home.html", context, context_instance=RequestContext(request))


def handle_redirect(request, *args, **kwargs):
    url_hash = kwargs.get('url_hash')

    try:
        url = Url.objects.get(url_hash=url_hash)
    except ObjectDoesNotExist, e:
        raise Http404

    actual_url = url.actual_url
    return redirect(actual_url)

        
        
        
        


