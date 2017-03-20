from django.shortcuts import render
from django import views


class ResumeView(views.View):
    def get(self, request):
        return render(request, 'resume.html', {})
