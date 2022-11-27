from django import forms
from .models import Article, Author, Tag

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

