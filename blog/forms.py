from django import forms                                                           

class PhotoForm(forms.Form):
	image = forms.ImageField(widget=forms.FileInput(attrs={'style' : 'display:none;'}),)
