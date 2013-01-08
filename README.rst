django-templatepages
--------------------

**django-templatepages** is a Django app for mapping URLs to templates
on the filesystem as if they were static web pages. This is useful
for integrating static content into your Django project while still
leveraging the Django templating language.

templatepages differs from django.contrib.flatpages in that the
content is stored entirely in templates on the filesystem, rather
than in a database. We developed this app to address a real-world
situation where much of the content in a project is static and
managed on the filesystem under version control. templatepages
allows us to factor out the page layout using the Django templating
language, and cleanly integrate the static content with other dynamic
components implemented as Django apps.

Python's ``mimetypes.guess_type()`` is used to determine appropriate
Content-type and Content-encoding headers for the HTTP response.
This means that you can use templatepages for more than just HTML
files; for example, we use it to serve dynamically-generated CSS
stylesheets.


Usage
-----

Using templatepages is relatively straightforward: just add it to
``INSTALLED_APPS`` in your project's settings.py file, and integrate
the URL mapping in your project's urls.py file. Then place your
templates in your project's templates/templatepages folder.

For example, the following stanza in urls.py will configure your
project to map all requests beginning with articles/ to
templatepages:

::

    urlpatterns = patterns('',
        (r'^articles/', include('templatepages.urls')),
    )

In this example, a request for http://your.site/articles/contact.html
should result in templatepages attempting to return a rendered
template based on ``templates/templatepages/contact.html``.
If this file cannot be found, templatepages will raise Http404.

If no filename is specified in the URL, templatepages will attempt
to render ``index.html``.

templatepages passes RequestContext to the template, so full access
to template context processor variables is available.
