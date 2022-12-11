from django.views import generic as views
from django.shortcuts import render


class NotFoundErrorView(views.View):
    def get(self, request):
        return render(request, 'errors/error404.html')


class InternalErrorView(views.View):
    def get(self, request):
        return render(request, 'errors/error404.html')