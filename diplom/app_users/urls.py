from django.urls import path
from app_users.views import UsersLogin, UsersLogout, Register, ProfileView, ListGroups, ListStudents, SolutionsStudent


urlpatterns = [
    path('login/', UsersLogin.as_view(), name='login'),
    path('logout/', UsersLogout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('groups/', ListGroups.as_view(), name='groups'),
    path('groups/<str:pk>/', ListStudents.as_view(), name='students'),
    path('groups/<str:pk>/<int:pk2>/', SolutionsStudent.as_view(), name='solutions'),
]
