from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 
        'workshop.posts.views.all_posts',
        name='all_posts'),
)
 
