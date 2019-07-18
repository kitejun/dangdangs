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
    # 요청 메서드가 POST방식 일 때만 처리
     if request.method == 'POST':
        # Post인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=post_pk)
        # request.POST에서 'content'키의 값을 가져옴
        content = request.POST.get('content')

        # 'content'키가 없었거나 내용이 입력되지 않았을 경우
        if not content:
            # 400(BadRequest)로 응답을 전송
            return HttpResponse('댓글 내용을 입력하세요', status=400)

    # 내용이 전달 된 경우, Comment객체를 생성 및 DB에 저장
    Comment.objects.create(
        post=post,
        # 작성자는 현재 요청의 사용자로 지정
        author=request.user,
        content=content
    )
        # 정상적으로 Comment가 생성된 후
        # 'post'네임스페이스를 가진 url의 'post_list'이름에 해당하는 뷰로 이동
        return redirect('post:post_list')