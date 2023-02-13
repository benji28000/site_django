from django import forms

class login_Form(forms.Form):
    username=forms.CharField(label="nom d'utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label="mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))


class register_Form(forms.Form):
    username=forms.CharField(label="nom d'utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label="mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_confirm=forms.CharField(label="confirmer le mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
