from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import Post,Comment
from .forms import CommentForm
from .utils import create_comment_tree


def base(request):
    comments = Post.objects.first().comments.all()
    result = create_comment_tree(comments)
    comment_form=CommentForm(request.POST or None)
    # for i in result:
    #     print (i , '\n')
    return render(
                    request,
                    'base.html',
                    {'comments':result,
                    'form':comment_form
                    } )


def create_comment(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.text= comment_form.cleaned_data['text']
        new_comment.content_type = ContentType.objects.get(model='post')
        new_comment.object_id = 1
        new_comment.parent  = None
        new_comment.is_child = False
        new_comment.save()
    return HttpResponseRedirect('/')


@transaction.atomic
def create_child_comment(request):
    user_name=request.POST.get('user')
    current_id=request.POST.get('id')
    text=request.POST.get('text')
    user=User.objects.get(username=user_name)
    content_type=ContentType.objects.get(model='post')
    parent=Comment.objects.get(id=int(current_id))
    is_child = False if not parent else True
    Comment.objects.create(
        user=user,
        text=text,
        content_type=content_type,
        object_id=1,
        parent=parent,
        child=is_child
    )
    comments_ = Post.objects.first().comments.all()
    comments_list=create_comment_tree(comments_)
    return render (request,'base.html',{'comments':comments_list})
