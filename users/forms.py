from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
from django.forms import TextInput
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from event.models import Event

from event.models import LinkEvent,Comments,EventFilePDF

from training.models import Training

from training.models import Document


from django import forms
# from .models import Comments


class CommentFormRedactor(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['event', 'author', 'text', 'status']
        widgets = {
            'event': forms.Select(attrs={'class': 'event-select'}),
            'author': forms.Select(attrs={'class': 'author-select'}),
            'text': forms.Textarea(attrs={'class': 'comment-textarea'}),
            'status': forms.CheckboxInput(attrs={'class': 'status-checkbox'}),
        }

class TrainingForm(forms.ModelForm):
    full_training = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Training
        fields = ['date_of_publication', 'slug', 'category', 'training_title', 'summary_training', 'full_training', 'links_training', 'video_training', 'graphic_illustrations']
        labels = {
            'date_of_publication': 'Дата публикации',
            'slug': 'Слаг',
            'category': 'Категория',
            'training_title': 'Заголовок',
            'summary_training': 'Краткое содержание',
            'full_training': 'Полный текст',
            'links_training': 'Ссылка на обучающие ресурсы',
            'video_training': 'Видео',
            'graphic_illustrations': 'Иллюстрация',
        }
        widgets = {
            'date_of_publication': forms.TextInput(attrs={'class': 'form-control','type': 'datetime-local','id': "my-datetime",'name':"my-datetime"}),
            'slug': forms.TextInput(attrs={'class': 'form-input form-control','type': "text"}),
            'category': forms.TextInput(attrs={'class': 'form-input form-control','type': "text"}),
            'training_title': forms.TextInput(attrs={'class': 'form-input form-control','type': "text"}),
            'summary_training': forms.TextInput(attrs={'class': 'form-input form-control','type': "text"}),
            'links_training': forms.URLInput(attrs={'class': 'form-control'}),
            'video_training': forms.FileInput(attrs={'class': 'form-control'}),
            'graphic_illustrations': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.Select(choices=Training.CATEGORY_CHOICES)

class LinkEventForm(forms.ModelForm):
    class Meta:
        model = LinkEvent
        fields = ['event', 'title', 'url']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-input form-control','type': "text"}),
            'title': forms.TextInput(attrs={'class': 'form-input form-control',
                                                                            'type': "text"}),
            'url': forms.URLInput(attrs={'class': 'form-input form-control',
                                                                            'type': "text"}),
        }
class EventForm(forms.ModelForm):
    text_event = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Event
        fields = ['date_event', 'category', 'slug', 'title_event','brief_announcement', 'text_event', 'place_realization',
                  'illustration_event','link_to_position']

        widgets = {
            'date_event': forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'id': "my-datetime",
                                                 'name': "my-datetime"}),
            'category': forms.Select(attrs={'class': 'form-input form-control', 'type': "text"}),
            'slug': forms.TextInput(attrs={'class': 'form-input form-control', 'type': "text"}),
            'title_event': forms.TextInput(attrs={'class': 'form-input form-control', 'type': "text"}),
            'brief_announcement': forms.TextInput(attrs={'class': 'form-input form-control', 'type': "text"}),

            'place_realization': forms.TextInput(attrs={'class': 'form-input form-control', 'type': "text"}),
            'illustration_event': forms.FileInput(attrs={'class': 'form-input form-control'}),
            'link_to_position': forms.URLInput(attrs={'class': 'form-input form-control', 'type': "text"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            for field in self.fields:
                self.fields[field].widget.attrs['value'] = getattr(instance, field)

class CustomCaptchaWidget(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': ''}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-input form-control',
                                                                         'type': "email", 'id': "email",
                                                                         'placeholder': "Введите ваш email"}))
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form-input form-control',
                                                                           'type': "text", 'id': "username",
                                                                           'placeholder': "Введите имя пользователя"}))
    last_name = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input form-control',
                                                                            'type': "text", 'id': "username",
                                                                            'placeholder': "Введите имя пользователя"}))
    first_name = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input form-control',
                                                                            'type': "text", 'id': "username",
                                                                            'placeholder': "Введите имя пользователя"}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput(
        attrs={'class': 'form-input form-control', 'type': "date", 'id': "birthdate"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'type': "password", 'id': "password",
               'placeholder': "Введите пароль"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'type': "password", 'id': "confirm-password",
               'placeholder': "Подтвердите пароль"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('email','username','date_of_birth','password1', 'password2','captcha')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form-input form-control','id': "login-username",'type':"text",'placeholder':"Введите ваш логин"}))
    # email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input form-control', 'type': "password", 'id':"password",'placeholder':"Введите пароль"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields =('username','password','captcha')



class EventFilePDFForm(forms.ModelForm):
    class Meta:
        model = EventFilePDF
        fields = ['event','title_file_pdf', 'file_event_pdf']
        labels = {
            'event':'Событие',
            'title_file_pdf': 'Текст к файлу',
            'file_event_pdf': 'Файлы',
        }
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'title_file_pdf': forms.TextInput(attrs={'class': 'form-control'}),
            'file_event_pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'file')