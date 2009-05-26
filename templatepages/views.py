import re
from mimetypes import guess_type
from django.conf import settings
from django.template import loader, RequestContext, TemplateDoesNotExist
from django.http import HttpResponse, Http404, get_host


# Hostnames should consist of longest string of letters, numbers, and dots at
# start of host header; this implies that port number and file path will be
# omitted
HOST_RE = re.compile('([a-z0-9][a-z0-9.]*[a-z0-9])')


def templatepage(request, url, template_dir='templatepages/', extra_context={}, context_processors=None):

    # If Django's APPEND_SLASH setting is enabled, and the URL does not end
    # with a slash or a file extension, Django will redirect to the URL with a
    # slash appended

    if template_dir and template_dir[-1] != '/':
        template_dir += '/'

    host = get_host(request).strip().lower()

    if host:
        try:
            template_host_dir = HOST_RE.match(host).groups()[0]
        except AttributeError:
            response = HttpResponse()
            response.status_code = 400
            response.write('[%s]' % get_host(request))
            return response
    else:
        template_host_dir = 'nohost'

    try:
        if settings.TEMPLATEPAGES_MULTISITE:
            prefix_list = (template_host_dir + '/', 'default/')
        else:
            prefix_list = ('',)
    except AttributeError:
        prefix_list = ('',)

    # Discard any bad segments in URL ("//", "/./". or "/../")
    clean_url = '/'.join([x for x in url.strip().split('/') if x not in ('','.','..')])

    for prefix in (prefix_list):
        try:
            t = loader.get_template(template_dir + prefix + clean_url)
            mimetype, encoding = guess_type(clean_url)
            break
        except TemplateDoesNotExist:
            pass
        try:
            t = loader.get_template(template_dir + prefix + clean_url + '/index.html')
            mimetype, encoding = guess_type('index.html')
            break
        except TemplateDoesNotExist:
            pass
    else:
        raise Http404

    context = RequestContext(request, {'url': url, 'host': host}, context_processors)
    if extra_context:
        for key, value in extra_context.items():
            if callable(value):
                context[key] = value()
            else:
                context[key] = value

    response = HttpResponse(t.render(context))
    response['Content-Type'] = mimetype or 'application/octet-stream'
    if encoding:
        response['Content-Encoding'] = encoding

    return response

