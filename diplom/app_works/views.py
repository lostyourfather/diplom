from app_works.models import Work, WorkUser, Image, File, Solution
from app_works.forms import WorkForm
from app_users.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage


class WorkCreate(View):

    def get(self, request, **kwargs):
        form = WorkForm()
        profiles = Profile.objects.all().values('group')
        groups = {user['group'] for user in profiles}
        return render(request, 'app_works/work_create.html', {'form': form, 'groups': groups})

    def post(self, request, **kwargs):
        form = WorkForm(request.POST)
        profiles = Profile.objects.all().values('group')
        groups = {user['group'] for user in profiles}
        if form.is_valid():
            #work_form = form.save()
            work = Work.objects.create(title=request.POST['title'], description=request.POST['description'])
            files = request.FILES.getlist('files')
            fs = FileSystemStorage(location='media/files/')
            for file in files:
                fs.save(file.name, file)
                File.objects.create(work=work, title=request.POST['file_title'], file=file.name)
            images = request.FILES.getlist('images')
            for image in images:
                fs.save(image.name, image)
                Image.objects.create(work=work, image=image.name)
            groups = request.POST.getlist('groups')
            for group in groups:
                users_id = Profile.objects.filter(group=group).all().values('user_id')
                for user_id in users_id:
                    WorkUser.objects.create(work=work, user=User.objects.get(id=user_id['user_id']))
            return redirect(f'/works/{work.id}')
        return render(request, 'app_users/work_create.html', {'form': form, 'groups': groups})


class WorkView(View):

    def get(self, requests, **kwargs):
        work_id = kwargs.get('pk')
        work = Work.objects.filter(id=work_id).first()
        images = Image.objects.filter(work=work_id).all()
        files = File.objects.filter(work=work_id).all()
        return render(requests, 'app_works/work.html', {'work': work, 'images': images, 'files': files})

    def post(self, requests, **kwargs):
        work_id = kwargs.get('pk')
        work = Work.objects.get(id=work_id)
        user_id = requests.user.id
        user = User.objects.get(id=user_id)
        file = requests.FILES.get('solution')
        Solution.objects.create(work=work, user=user, file=file.name)
        fs = FileSystemStorage(location='media/files/')
        fs.save(file.name, file)
        images = Image.objects.filter(work=work_id).all()
        files = File.objects.filter(work=work_id).all()
        return render(requests, 'app_works/work.html', {'work': work, 'images': images, 'files': files})
