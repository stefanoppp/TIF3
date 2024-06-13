from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', exit, name='exit'),
    path('train/', train, name='train'),
    path('train/developer/', developer_mode, name='developer_mode'),
    path('train/automatic/', automatic_mode, name='automatic_mode'),
    path('train/process_developer_mode/', process_developer_mode, name='process_developer_mode'),
]