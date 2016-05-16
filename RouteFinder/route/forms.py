 # -*- coding: utf-8 -*-
from django import forms

from .models import Edge,Stopage

class RouteForm(forms.Form):
    source=forms.ModelChoiceField(queryset=Stopage.objects.all().order_by('name'))
    destination=forms.ModelChoiceField(queryset=Stopage.objects.all().order_by('name'))


#
# class CreatePostForm(forms.ModelForm):
#
# 	title=forms.CharField(label='শিরোনাম')
# 	content=forms.CharField(widget=forms.Textarea,label='লেখা')
#
# 	class Meta:
# 		model = Post
# 		fields = ['title', 'user','content']
# 		### exclude = ['full_name']
