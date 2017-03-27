from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify
from rango.models import UserProfile,restrict
import itertools
class UserForm(forms.ModelForm):
 password = forms.CharField(widget=forms.PasswordInput())

 class Meta:
  model = User
  email ={ 'required':True}
  first_name={'required':True}
  last_name={'required':True}
  fields = ('username','email','password','first_name','last_name')

class UserProfileForm(forms.ModelForm):
 class Meta:
  model = UserProfile
  fields = ('picture',)
class blogform(forms.ModelForm):
 name=forms.CharField(label='Blog name',max_length=128)
 views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
 likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
 body=forms.CharField(widget=forms.Textarea)
 
 class Meta:
  model = restrict
  fields = ('name','body',)
 def save(self):
        instance = super(blogform, self).save(commit=False)
        instance.slug=orig=slugify(instance.name)
        for x in itertools.count(1):
         if not restrict.objects.filter(slug=instance.slug).exists():
          break
         instance.slug = '%s-%d' % (orig,x)
        instance.save()
        return instance
