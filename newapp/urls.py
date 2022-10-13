from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),

]