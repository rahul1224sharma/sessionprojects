from django import forms

class LoginForm(forms.Form):
    name=forms.CharField(max_length=30)


class ItemAddForm(forms.Form):
    name=forms.CharField(max_length=30)
    quantity=forms.IntegerField()

class NameForm(forms.Form):
    name=forms.CharField()

class AgeForm(forms.Form):
    age=forms.IntegerField()

class ParentForm(forms.Form):
    pname=forms.CharField()

class AddItemForm(forms.Form):
    name=forms.CharField(max_length=30)
    quantity=forms.IntegerField()