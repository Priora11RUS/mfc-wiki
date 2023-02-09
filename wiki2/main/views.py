from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import AddPostForm, RegisterUserForm, PasswordChageViewForm
from .models import *
from.utils import *

# Список статей на одной странице
class FeedHtml(ListView):
    model = Post
    paginate_by = 10 # Количество элементов на одной странице
    template_name = 'Wiki/feed.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context ['wiki'] = 'Публикации — Wiki'
        return context

# Список всех публикаций
class ListFeed(ListView):
    model = Post
    template_name = 'Wiki/allfeed.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context ['wiki'] = 'Все публикации — Wiki'
        return context

def index(request):
    if 'term' in request.GET:
        objectlist = Post.objects.filter(
            Q(title__icontains=request.GET.get('term')) |
            Q(content__icontains=request.GET.get('term')))
        titles = list()
        for post in objectlist:
            titles.append(post.title)
        return JsonResponse(titles, safe=False)

    dictionary = {
        'title':'Главная | Wiki'
    }
    return render(request,'wiki/main.html', context=dictionary)

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    content = {
        'post': post,
        'title': post.title # Заголовок статьи
    }
    return render(request, 'wiki/post.html', context=content) # Отоброжение веб страницы

# Добавление статьи
class AddNewPost(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Post
    form_class = AddPostForm
    template_name = 'wiki/add_post.html'
    permission_required = ('main.add_post')
    

# Автор поста
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save
        return super().form_valid(form)

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context ['wiki'] = 'Новая статья — Wiki'
        return context

# Загрузка файлов
    def upload(request):
        if request.method == 'POST':
            form = AddNewPost(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('wiki/add_post.html')
        else:
            form = AddNewPost()
        return render(request, 'wiki/add_post.html', {'form': form})


# Редактирование статьи
class UpdatePost(PermissionRequiredMixin, UpdateView): 
    model = Post
    form_class = AddPostForm
    template_name = 'wiki/edit_post.html'
    permission_required = ('main.change_post')

# Удаление статьи
def delete_page(request, id):
    record = Post.objects.get(id=id)
    record.delete()
    return redirect(reverse('feed'))
    
def pageNotFound(request, execption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# Регистрация и авторизация пользователя
def RegisterUser(request):
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Создан аккаунт {username}')
                return redirect('login')
        else:
            form = RegisterUserForm()
        regist_user = {
            'form': form,
            'title': 'Регистрация'
        }
        return render(request, 'wiki/register.html', context=regist_user)

# Смена пароля в профиле пользователя
class PasswordChageProfile(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChageViewForm
    template_name = 'wiki/profile.html'
    success_message = "Ваш пароль был успешно изменен"
    success_url = reverse_lazy('profile')
    
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context ['title'] = 'Личный кабинет'
        return context


# Поиск на главной странице
class SearchResultsView(ListView):
    model = Post
    template_name = 'wiki/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
         )
        return object_list

# Авторизация    
def login(request):
    dictionary = {
        'title':'Авторизация'
    }
    return render(request,'wiki/login.html', context=dictionary)