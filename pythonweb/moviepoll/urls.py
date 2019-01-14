from django.urls import path
from .views import index, detail, result

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:question_id>', detail, name='detail'),
    path('result/', result, name='result'),
]