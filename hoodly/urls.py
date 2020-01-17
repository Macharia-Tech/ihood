from django.conf.urls import url
from . import views 


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^post/(\d+)',views.single_post, name='post'),
    url(r'^add/postt$', views.add_post, name='add-post'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'displayprofile/(?P<user_id>\d+)$',views.display_profile,name='displayprofile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/post/$', views.PostList.as_view()),
]