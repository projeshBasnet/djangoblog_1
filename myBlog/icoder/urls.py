
from django.urls import path, include
from icoder import views
from .views import (Homeview, 
    PostView, 
    Createpostview, 
    Updatepostview, 
    PostDeleteView,
    UserPostListView

)


urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('post/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostView.as_view(), name='detail-post'),
    path('post/new/', Createpostview.as_view(), name='create-post'),
    path('post/<int:pk>/update', Updatepostview.as_view(), name='update-post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post'),
    path('about/', views.about, name='about'),
]
