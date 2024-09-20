from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Post
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request,'home.html')

def post(request):
    posts = Post.objects.all()
    return render(request,'post.html',{'post':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            content = request.POST['content']
            # Menggunakan user yang sedang login sebagai author
            author = request.user
            
            # Membuat dan menyimpan post baru
            Post.objects.create(title=title, content=content, author=author)
            print("data berhasil di buat")
            return redirect('post')  # Setelah berhasil, redirect ke halaman daftar post
        except IntegrityError as e:
            print(e)
            return redirect('post')
    return render(request, 'create_post.html')

@login_required
def delete_post(request, post_title):
    post = get_object_or_404(Post, content=post_title)

    # Memastikan hanya pemilik post yang dapat menghapusnya
    if request.user == post.author:
        post.delete()  # Menghapus post
        return redirect('post')  # Redirect setelah berhasil
    else:
        return redirect('index')
    
@login_required
def update_post(request, post_title):
    post = get_object_or_404(Post, content=post_title)

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
        return redirect('post')  

    return render(request, 'update_post.html', { 'post': post})


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ganti dengan nama URL tujuan Anda
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')  # Ganti dengan nama URL tujuan Anda
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 