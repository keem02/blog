from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.db.models import Q


# def post_list(request):
#     posts = Post.objects.all().order_by("-created_at")
#     return render(request, "blog/post_list.html", {"posts": posts})
def post_list(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by("-created_at")
    else:
        posts = Post.objects.all().order_by("-created_at")

    return render(request, "blog/post_list.html", {"posts": posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "blog/delete_post.html", {"post": post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form, "post": post})
