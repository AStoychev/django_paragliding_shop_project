from django.urls import path, include

from paragliding_shop.accounts.views import index, SignInView, SignUpView, \
    SignOutView, UserDetailsView, \
    UserEditView, UserDeleteView, show_order, AllUsers

urlpatterns = (
    path('', index, name='index'),
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('all-users/', AllUsers.as_view(), name='all users'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
        path('basket/', show_order, name='basket'),
        # path('basket/', show_order, name='basket'),
    ])),
)
