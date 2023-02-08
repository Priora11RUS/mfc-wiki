from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from main.forms import CustomLoginForm

urlpatterns = [
    path('', views.index, name='home'), # Главная страница
    path('add-new/', views.AddNewPost.as_view(), name='add_new'), # Вкладка новой статьи
    path('feed/', views.FeedHtml.as_view(), name='feed'), # Список публикаций
    path('login/', LoginView.as_view(template_name='wiki/login.html', authentication_form=CustomLoginForm), name='login'), # Авторизация
    path('logout/', LogoutView.as_view(template_name='wiki/logout.html'), name='logout'), # Выход из системы
    path('register/', views.RegisterUser, name='register'), # Регистрация
    path('post/<slug:post_slug>/', views.show_post, name='myurl'), # Отоброжение сделано по слаг, имя slug может быть любым (post_slug)
    path('profile/', views.PasswordChageProfile.as_view(), name='profile'), # Профиль пользователя
    path('search/', views.SearchResultsView.as_view(), name='search_results'), # Страница поиска
    path('delete-page/<int:id>', views.delete_page, name='delete_page'), # Удаление статьи
    path('update/<int:pk>/', views.UpdatePost.as_view(), name='edit_post')
    ]