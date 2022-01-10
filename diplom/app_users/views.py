from app_users.models import Profile
from app_users.forms import RegisterForm
from app_works.models import WorkUser, Work, Solution
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class UsersLogin(LoginView):
    template_name = 'app_users/login.html'


class UsersLogout(LogoutView):
    template_name = 'app_users/login.html'


class Register(View):
    def get(self, request, **kwargs):
        form = RegisterForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request, **kwargs):
        form = RegisterForm(request.POST)
        fs = FileSystemStorage(location='media/files/')
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, phone_number=request.POST['phone_num'], group=request.POST['group'], avatar=request.FILES.get('avatar').name)
            fs.save(request.FILES.get('avatar').name, request.FILES.get('avatar'))
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=password)
            login(request, user)
            return redirect('/users/profile')
        return render(request, 'app_users/register.html', {'form': form})


class ProfileView(View):

    def get(self, request, **kwargs):
        id = self.request.user.id
        user = User.objects.get(id=id)
        works = WorkUser.objects.filter(user=id).all()
        works = [(work.work.id, work.grade if work.grade is not None else 'no result', Work.objects.get(id=work.work.id).title) for work in works]
        if Profile.objects.filter(user=id).exists():
            profile = Profile.objects.get(user=id)
            return render(request, 'app_users/profile.html', {'user': user, 'profile': profile, 'works': works})
        else:
            return render(request, 'app_users/profile.html', {'user': user})


class ListGroups(View):

    def get(self, request):
        groups = (profile.group for profile in Profile.objects.all())
        return render(request, 'app_users/groups.html', {'groups': groups})


class ListStudents(View):

    def get(self, request, **kwargs):
        group = kwargs.get('pk')
        profiles = Profile.objects.filter(group=group).all()
        users = [User.objects.get(id=profile.user.id) for profile in profiles]
        return render(request, 'app_users/students.html', {'students': users, 'group': group})


class SolutionsStudent(View):

    def get(self, request, **kwargs):
        student_id = kwargs.get('pk2')
        solutions = Solution.objects.filter(user=student_id).all()
        solutions = [[solution.file, Work.objects.get(id=solution.work.id).title] for solution in solutions]
        return render(request, 'app_users/solutions.html', {'solutions': solutions})

    def post(self, request, **kwargs):
        works = {work[0].replace('grade-', ''): work[1] for work in request.POST.items() if 'grade-' in work[0]}
        student_id = kwargs.get('pk2')
        for work in works.items():
            work_id = Work.objects.filter(title=work[0]).first().id
            sol_work = WorkUser.objects.filter(user=student_id, work=work_id).first()
            print(sol_work)
            sol_work.grade = work[1]
            sol_work.save()
        solutions = Solution.objects.filter(user=student_id).all()
        solutions = [[solution.file, Work.objects.get(id=solution.work.id).title] for solution in solutions]
        return render(request, 'app_users/solutions.html', {'solutions': solutions})