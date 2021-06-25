from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import PostAddForm
from .models import Bidd ,Post

# Create your views here.



def home_view(request):
    posts = Post.objects.all()
    return render(request, "post/home.html", {"posts": posts})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "successful")
            return redirect("posts:home")
        else:
            return render(request, "post/add_post.html", {"form": form})
    else:

        form = PostAddForm()
        return render(request, "post/add_post.html", {"form": form})



@login_required
@csrf_exempt
def add_bidd(request):
    post_id = request.POST.get('post_id')
    bidd_amt = request.POST.get('amt')
    bidd_des = request.POST.get('des')

    post = get_object_or_404(Post, id = post_id)
    user = request.user

    Bidd.objects.create(user=user, post=post, bidd_amt=bidd_amt,bidd_des=bidd_des)
    return JsonResponse({'user':user.first_name, 'bidd_amt':bidd_amt,})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user == post.user:
        post.delete()
        next = request.GET.get('next', '/')
        return redirect(next)
    else:
        return HttpResponseNotFound()

