from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
 

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))

    class Meta:
        model = Post
        fields = ('title','overview','content','thumbnail_picture','categories','featured','previous_post','next_post')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea( attrs = {
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': 5,
    }))
    class Meta:
        model = Comment
        fields = ('content',)