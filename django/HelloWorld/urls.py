from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('views',
    url(r'^hello$', 'index'),
    url(r'^dtl_hello$', 'dtl_hello'),
    url(r'^dtl_sql$', 'dtl_sql'),
)
