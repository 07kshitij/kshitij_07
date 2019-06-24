from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name="post_publish"),
    path('post/<pk>/remove/', views.post_remove, name="post_remove"),
    path('CP/', views.cp, name='cp'),
    path('ML/', views.ml, name='ml'),
    path('AllPosts/', views.all, name='all'),
    path('about_me/', views.about_me, name='about_me'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',
            views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',
            views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',
            views.comment_remove, name='comment_remove'),
    re_path(r'^post/(?P<pk>\d+)/upvote/$', views.upvote, name='upvote'),
    re_path(r'^post/(?P<pk>\d+)/downvote/$', views.downvote, name='downvote'),
    re_path(r'^post/(?P<pk>\d+)/down/$', views.down, name='down'),
    re_path(r'^post/(?P<pk>\d+)/up$', views.up, name='up'),
]
