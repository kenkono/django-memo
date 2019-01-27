from django.forms import ModelForm
from .models import Memo
from django.contrib.auth.forms import AuthenticationForm


class MemoForm(ModelForm):
	class Meta:
		model = Memo
		fields = ['title', 'text']


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
