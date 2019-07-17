from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Board, Comment
from .forms import BoardPost, CommentForm

# Create your views here.
def board(request):
    boards=Board.objects
    board_list=Board.objects.all()
    paginator = Paginator(board_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'board.html',{'boards':boards,'posts':posts})


def detail(request, board_id):
    details = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'post': post})


def new(request):
    if  request.method == 'POST' :
        form = BoardPost(request.POST)
        if form.is_valid:
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            like=0
            post.save()
            return redirect('board')

    else :
        form = BoardPost() 
        return render(request,'new.html',{'form':form})



def update(request,board_id):
    board=get_object_or_404(Board,pk=board_id)

    form = BoardPost(request.POST,instance=board)
    
    if form.is_valid():
        form.save()
        return redirect('board')

    return render(request,'input.html',{'form':form})

def delete(request,board_id):
    board=get_object_or_404(Board,pk=board_id)
    board.delete()
    return redirect('board')

# comment 부분 시작
def comment_new(request, board_id):
    if request.method == 'POST' :
        form = BoardPost(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.post = Board.objects.get(pk=board_id)
            comment.save()
            return redirect('detail', board_id)
    else :
        form = CommentForm() 
    return render(request,'comment_new.html',{'form':form})