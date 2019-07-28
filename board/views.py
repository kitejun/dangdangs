from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage

from .models import Post, Comment
from .forms import PostForm, PostSearchForm, CommentForm
from django.views.generic.edit import FormView
from django.db.models import Q
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
    board=Post.objects.get(id=board_id)

    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():


            print(form.cleaned_data)
            board.title = form.cleaned_data['title']
            board.context = form.cleaned_data['context']
            board.image = form.cleaned_data['image']
            board.updated_at = timezone.now()

            board.save()
            return redirect('board')
        
    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = PostForm(instance = board)
        # 기존 내용 불러오기
        context={
            'form':form,
            'writing':True,
            'now':'update',
        }
        return render(request, 'update.html',{'form':form})
        

def delete(request,board_id):
    board=get_object_or_404(Post,pk=board_id)
    board.delete()
    return redirect('board')



class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'board.html'

    def form_valid(self, form):
        search_word = self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=search_word) | Q(context__icontains=search_word))

        context = {}
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
    

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
        