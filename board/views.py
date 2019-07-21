from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def board(request):
    boards=Post.objects

    board_list=Post.objects.all()
    paginator = Paginator(board_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)



    return render(request,'board.html',{'boards':boards,'posts':posts})


def detail(request, board_id):
    board_detail = get_object_or_404(Post, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})


def new(request):
    if  request.method == 'POST' :
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post=form.save(commit=False)
            post.created_at=timezone.now()
            post.updated_at=timezone.now()
            post.save()
            return redirect('board')

    else :
        form = PostForm() 
        return render(request,'new.html',{'form':form})



def update(request,board_id):
    board=get_object_or_404(Post,pk=board_id)

    form = PostForm(request.POST,instance=Post)
    
    if form.is_valid():
        post.updated_at=timezone.now()
        form.save()
        return redirect('board')

    return render(request,'new.html',{'form':form})

def delete(request,board_id):
    board=get_object_or_404(Post,pk=board_id)
    board.delete()
    return redirect('board')

# comment 부분 시작
def comment_new(request, board_id):
    # 요청 메서드가 POST방식 일 때만 처리
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Post.objects.get(pk=board_id)
        comment.save()
        return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 'new_comment.html',{
        'form':form,
    })
        