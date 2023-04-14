from django import forms
from django.forms import Textarea

from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'class': 'form-input form-control',
                                                                          'type': "text", 'id': "comment",'rows':"5",
                                                                          'placeholder': "Введите ваш Комментарий"})

