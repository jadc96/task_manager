from django.forms import ModelForm
from .models import TaskCategory, Task, User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class TaskCategoryForm(ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
