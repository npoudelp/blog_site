from django.urls import path
from api import apis


urlpatterns = [
    path('', apis.get_all, name='get_all'),
    path('get_by_id/<int:id>', apis.get_by_id, name='get_by_id'),
    path('post_blog/', apis.post_blog, name='post_blog'),
    path('edit_blog/<int:id>', apis.edit_blog, name='edit_blog'),
]