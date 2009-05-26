from django.conf.urls.defaults import patterns


urlpatterns = patterns('',

    (r'^(?P<url>.*)$', 'templatepages.views.templatepage'),

)
