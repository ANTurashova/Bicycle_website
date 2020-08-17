from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    """Форма комментариев"""

    class Meta:
        model = Comment  # От какой модели строим
        fields = ("email", "name", "text")  # Какие поля из модели будут в форме


