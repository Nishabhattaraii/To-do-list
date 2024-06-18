from django import forms

#class userforms(forms.Form):
 #num1=forms.CharField(label="username",required=False,widget=forms.TextInput(attrs=))

class userForms(forms.Form):
 num1=forms.CharField(label="username",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
 num2= num1=forms.CharField(label="password",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
