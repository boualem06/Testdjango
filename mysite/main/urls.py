# urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('articles',views.ArticleViewSet,basename='articles')
router.register('users',views.UserViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    

    
    # path('articles/', views.article_list, name='article_list'),
    # path('articles/<int:pk>', views.article_details, name='article_details'),
    # path('articles/', views.ArticleList.as_view()),
    # path('articles/<int:id>', views.ArticleDetails.as_view()),
]