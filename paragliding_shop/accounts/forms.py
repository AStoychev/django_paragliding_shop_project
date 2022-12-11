from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


UserModel = get_user_model()
placeholders = {
    'username': "Username",
}


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}
        widgets = {
            'image': forms.FileInput()
        }


class UserCreateForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'country', 'image', 'age')
        field_classes = {'username': auth_forms.UsernameField}
        widgets = {
            'password': forms.PasswordInput()
        }