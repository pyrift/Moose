from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'message']
        exclude = ['post']
    def __init__(self, *args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        for fild_name, fild in self.fields.items():
            fild.widget.attrs['class'] = 'form-control'
            fild.widget.attrs['placeholder'] = fild_name