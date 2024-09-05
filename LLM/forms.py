from django import forms


class RecipeForm(forms.Form):
    my_message = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Ask your Question about python'}))
