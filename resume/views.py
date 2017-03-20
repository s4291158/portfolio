from django.shortcuts import render
from django import views


class ResumeView(views.View):
    def get(self, request):
        context = {
        }
        return render(request, 'resume.html', context)


class ProfileView(views.View):
    def get(self, request):
        context = {
        }
        return render(request, 'profile.html', context)
