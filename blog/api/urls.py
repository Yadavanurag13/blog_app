from django.urls import path, include
from account.views import *

urlpatterns = [
    path('account/', include('account.urls'))
]
