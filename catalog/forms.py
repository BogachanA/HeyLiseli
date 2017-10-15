from django import forms
import re
from catalog.models import Liseli, Lise
from registration.forms import RegistrationFormUniqueEmail

class loginForm(forms.Form):
    auto_id=False

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Kullanıcı Adın',}),max_length=100,required=True,label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Şifren'}),label='')


class registerForm(RegistrationFormUniqueEmail):
    auto_id=False

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Adın', 'class':'inputField','id':'nameInput'}),max_length=100,required=True,label='')
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Soyadın', 'class':'inputField','id':'surnameInput'}),max_length=100,required=True,label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Kullanıcı Adın', 'class':'inputField','id':'userInput'}),max_length=100,required=True,label='')
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'E-mail adresin','class':'inputField ','id':'emailInput'}),required=True,label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Şifren','class':'inputField','id':'passInput'}),required=True,label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Şifreni Tekrarla','class':'inputField','id':'rePassInput'}),required=True,label='')
    grade = forms.CharField(widget=forms.Select(choices=Liseli.GRADE_CHOICES),label='')
    lise = forms.ModelChoiceField(queryset=Lise.objects.all().order_by('name'),empty_label=None,required=False,widget=forms.Select(attrs={'id':'schoolSelect'}),label='')
    newSchool = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Okulunun Adı', 'class': 'inputField d-none', 'id': 'newSchoolInput'}), required=False,label='')


    class Meta:
        model = Liseli
        fields = ('name', 'surname', 'username', 'email', 'password1', 'password2', 'grade', 'lise', 'newSchool')


    def clean_username(self):
        data = self.cleaned_data['username']
        username_regex=re.compile("^[a-zA-ZığüşöçĞÜŞÖÇİ@\-_\.0-9]{6,}$")
        if not username_regex.match(data):
            raise forms.ValidationError("◊ Kullanıcı adın 6 veya daha fazla karakterden oluşmalıdır ve boşluk içeremez. İçerebileceği özel karakterler: @, -, _ ve .")
        if Liseli.objects.filter(username=data).exists():
            raise forms.ValidationError("◊ Seçtiğin kullanıcı adını bir başka liseli almış :/ Daha farklı bir kullanıcı adı dene.")
        return data

    def clean_email(self):
        data=self.cleaned_data['email']
        email_regex=re.compile("^[a-zA-Z@\-_\.0-9]+@[\w]+\.[\w\.]+$")
        if not email_regex.match(data):
            raise forms.ValidationError("◊ Lütfen geçerli bir e-mail adresi gir liseli.")
        if Liseli.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("◊ Bu e-mail adresi çoktan kullanımda! Yoksa yine şifreni mi unuttun?")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        pass_regex=re.compile("^[\w!\.\,*\-_@ığüşöçĞÜŞÖÇİ]{6,}$")
        if not pass_regex.match(data):
            raise forms.ValidationError("◊ Şifrenin 6 karakter veya daha fazlasını içerdiğinden emin ol. İçerebileceği özel karakterler: !, @, -, _, *, '.' ve ',' ")
        return data

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("◊ Girdiğin şifreler birbirini tutmuyor. Uykusuzsun yine sanırım?")
        return password2

    def clean_grade(self):
        data=self.cleaned_data['grade']
        if data and data=="Choose":
            raise forms.ValidationError("◊ Sınıfını seçmeyi unuttun. Dalgınlığın üzerinde bakıyorum..")
        return data

    def clean_lise(self):
        data=self.cleaned_data['lise']
        if data.name=="--Okulunu Seç--":
            if not self['newSchool'].value():
                raise forms.ValidationError("◊ Dostum! Ya listeden bir okul seç, ya da bulamadıysan listenin altındaki kutucuğa okulunun adını yaz.")
            else:
                new_lise, created=Lise.objects.get_or_create(name=self['newSchool'].value())
                data=new_lise
        return data


class social_auth_complete(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'extraInput','id':'extraEmail','placeholder':'E-mail Adresin'}),label='',required=True)
    grade = forms.CharField(widget=forms.Select(choices=Liseli.GRADE_CHOICES,attrs={'id':'gradeSelect'}), label='')
    lise = forms.ModelChoiceField(queryset=Lise.objects.all().order_by('name'), empty_label=None, required=False,
                                  widget=forms.Select(attrs={'id': 'schoolSelect'}), label='')
    newSchool = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Okulunun Adı', 'class': 'extraInput', 'id': 'newSchoolInput'}), required=False,
                                label='')

    def clean_email(self):
        data=self.cleaned_data['email']
        email_regex=re.compile("^[a-zA-Z\-_\.0-9]+@[\w]+\.[\w\.]+$")
        if not email_regex.match(data):
            raise forms.ValidationError("◊ Lütfen geçerli bir e-mail adresi gir liseli.")
        if Liseli.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("◊ Bu e-mail adresi çoktan kullanımda! Yoksa yine şifreni mi unuttun?")
        return data

    def clean_grade(self):
        data=self.cleaned_data['grade']
        if data=="Choose":
            raise forms.ValidationError("◊ Sınıfını seçmeyi unuttun. Dalgınlığın üzerinde bakıyorum..")
        return data

    def clean_lise(self):
        data=self.cleaned_data['lise']
        if data.name=="--Okulunu Seç--":
            if not self['newSchool'].value():
                raise forms.ValidationError("◊ Dostum! Ya listeden bir okul seç, ya da bulamadıysan listenin altındaki kutucuğa okulunun adını yaz.")
            else:
                new_lise, created=Lise.objects.get_or_create(name=self['newSchool'].value())
                data=new_lise
        return data

class applyToInternship(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'applyInput textInput','id':'applyName','placeholder':'Adın'}),max_length=200,required=True,label='')
    surname=forms.CharField(widget=forms.TextInput(attrs={'class':'applyInput textInput','id':'applySurname','placeholder':'Soyadın'}),max_length=200,required=True,label='')
    school=forms.CharField(widget=forms.TextInput(attrs={'class':'applyInput textInput','id':'applySchool','placeholder':'Okulunun Adı'}),max_length=200,required=True,label='')
    mail=forms.EmailField(widget=forms.EmailInput(attrs={'class':'applyInput textInput','id':'applyEmail','placeholder':'E-mail Adresin'}),max_length=300,required=True,label='')
    grade=forms.CharField(widget=forms.Select(choices=Liseli.GRADE_CHOICES,attrs={'class':'applyInput selectInput','id':'applyGrade'}),label='',required=True)
    resume=forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'applyInput fileInput','id':'applyResume'}),required=True,label='')
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'applyInput textAreaInput','id':'applyMessage','placeholder':'En fazla 500 karakter lütfen. Dramatik olmaya gerek yok...'}),required=True,label='')

