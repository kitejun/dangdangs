from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

from .models import Posting
from .forms import PostingPost

# Create your views here.

def home(request):
    return render(request,'home.html')

def board(request):
    boards=Posting.objects

    board_list=Posting.objects.all()
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
    board_detail = get_object_or_404(Posting, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})


def new(request):
    if  request.method == 'POST' :
        form = PostingPost(request.POST, request.FILES)
        if form.is_valid:
            post=form.save(commit=False)
            post.createed_at=timezone.now()
            post.save()
            return redirect('board')

    else :
        form = PostingPost() 
        return render(request,'input.html',{'form':form})



def update(request,board_id):
    board=get_object_or_404(Posting,pk=board_id)

    form = PostingPost(request.POST,instance=Posting)
    
    if form.is_valid():
        post.updated_at=timezone.now()
        form.save()
        return redirect('board')

    return render(request,'input.html',{'form':form})

def delete(request,board_id):
    board=get_object_or_404(Posting,pk=board_id)
    board.delete()
    return redirect('board')