

from django.urls import path

from .views import *

urlpatterns = [  
    path('', InfoHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', InfoCategory.as_view(), name='category'),

    


]
