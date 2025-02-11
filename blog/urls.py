from django.urls import path
from .views import create_post, post_list, post_detail, edit_post, delete_post

urlpatterns = [
    path("", post_list, name="post_list"),  # 변경: '/' 경로를 게시글 목록으로 설정
    path("create/", create_post, name="create_post"),
    # 추가: 상세 페이지, 수정, 삭제를 위한 URL 패턴
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", edit_post, name="edit_post"),
    path("post/<int:pk>/delete/", delete_post, name="delete_post"),
]
