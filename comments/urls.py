from django.urls import path
from . views import *

urlpatterns = [
    path('',base),
    path('create-comment/',create_comment,name='comment-create'),
    path('create-child-comment/',create_child_comment,name='comment-child-create'),
]