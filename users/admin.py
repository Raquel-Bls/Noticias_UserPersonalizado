from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUser, CustomUserChangeForm, CustomUserCreationFrom
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    auth_form = CustomUserCreationFrom
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ['is_staff', 'username', 'email', 'Nombre']


admin.site.register(CustomUser, CustomUserAdmin)
