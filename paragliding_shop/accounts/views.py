from django.template import loader
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views, get_user_model, login

from paragliding_shop.accounts.models import AppUser
from paragliding_shop.accounts.forms import UserCreateForm
from paragliding_shop.equipment.models import Wings

UserModel = get_user_model()


# class InternalErrorView(views.View):
#     def get(self, request):
#         return render(request, 'errors/error404.html')


def index(request):
    return render(request, 'index.html')


def show_order(request, pk):
    current_user = AppUser.objects.get(pk=pk)
    start_price = current_user.order
    wings = Wings.objects.all()

    context = {
        "current_user": current_user,
        "start_price": start_price,
        "wings": wings,
    }

    return render(request, 'accounts/basket.html', context)


class AllUsers(LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'accounts/all-users.html'
    default_paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('dashboard')


class SignUpView(views.CreateView):
    model = UserModel
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        try:
            login(request, self.object)
        except:
            pass
        return response


class SignOutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        context['is_superuser'] = self.request.user.is_superuser

        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'age', 'image', 'country', 'gender')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        context['is_superuser'] = self.request.user.is_superuser

        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        context['is_superuser'] = self.request.user.is_superuser

        return context
