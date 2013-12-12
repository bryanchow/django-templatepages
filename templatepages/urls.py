from django.conf.urls import patterns


urlpatterns = patterns('',

    (r'^(?P<url>.*)$', 'templatepages.views.templatepage'),

)
