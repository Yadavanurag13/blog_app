from django.urls import path
from home.views import *

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog-list-create'),
    path('public/', PublicView.as_view(), name='public-blog-list')
]