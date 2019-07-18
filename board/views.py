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
    comments = Comment.objects
    return render(request, 'detail.html', {'details': details, 'comments':comments, })


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

def delete(request,board_id):
    board=get_object_or_404(Board,pk=board_id)
    board.delete()
    return redirect('board')

# comment 부분 시작
def comment_new(request, board_id):
    # 요청 메서드가 POST방식 일 때만 처리
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Board.objects.get(pk=board_id)
        comment.save()
        return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 'new_comment.html',{
        'form':form,
    })
        