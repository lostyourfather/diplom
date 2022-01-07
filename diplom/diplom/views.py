from django.shortcuts import render, redirect


def start_page(request):
    if request.user.is_authenticated:
        return redirect('/users/profile/')
    return redirect('/users/login/')
