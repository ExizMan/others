"""Определяет схемы URL для learning_logs"""
from django.urls import path
from . import views 

app_name='learning_logs'
urlpatterns = [
    #домашняя страница
    path('',views.index, name='index'),
    #topics
    path('topics/',views.topics,name='topics'),
    #idtopics
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
]