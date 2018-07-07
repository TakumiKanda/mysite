from django import forms                                                           

class PhotoForm(forms.Form):
	image = forms.ImageField(label = '', widget=forms.FileInput(attrs={'style' : 'display:none;'}),)
