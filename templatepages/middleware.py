from templatepages.views import templatepage
from django.http import Http404
from django.conf import settings


class TemplatepageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for a templatepage for non-404 responses.
        try:
            return templatepage(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
