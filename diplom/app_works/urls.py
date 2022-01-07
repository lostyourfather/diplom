from django.urls import path
from app_works.views import WorkCreate, WorkView


urlpatterns = [
    path('create/', WorkCreate.as_view(), name='work_create'),
    path('<int:pk>/', WorkView.as_view(), name='work_create'),
]
