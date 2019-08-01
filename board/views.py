from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

# 파일 저장 import문
from django.core.files.storage import FileSystemStorage

from .models import Board, Comment
from .forms import BoardPost


def home(request):
    return render(request, 'home.html')

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
    return render(request, 'detail.html', {'details': details})


def new(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            # 날짜는 자동으로 현재 입력해주는 것
            post.pub_date = timezone.now()
            post.save()
            return redirect('board')     # 바로 home으로 redirect
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = BoardPost()
        return render(request, 'new.html', {'form':form}) # form형태로 전달


# 수정하기
def update(request,board_id):
    post=Board.objects.get(id=board_id)

    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid(): #error
                
            # 검증에 성공한 값들은 사전타입으로 제공 
            print(form.cleaned_data)
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.image = form.cleaned_data['image']
            post.pub_date = timezone.now()

            post.save()
            return redirect('board')

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BoardPost(instance = post)
        # 기존 내용 불러오기
        context={
            'form':form,
            'writing':True,
            'now':'update',
        }
        return render(request, 'update.html',{'form':form})

# 삭제하기
def delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('board')

def comment_write(request, board_id):
    if request.method == 'POST':
        board = get_object_or_404(Board, pk=board_id)
        content = request.POST.get('content')

        Comment.objects.create(board=board, comment_body=content)
        return redirect('/board/detail/' + str(board.id))