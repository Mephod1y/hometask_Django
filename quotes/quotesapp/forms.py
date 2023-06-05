from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, ModelMultipleChoiceField
from .models import Quote, Author, Tag, User


class TagForm(ModelForm):
    tag = CharField(max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']


class QuoteForm(ModelForm):
    author = ModelChoiceField(queryset=Author.objects.none())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.none())

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    def __init__(self, user: User, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(user=user)
        self.fields['tags'].queryset = Tag.objects.all()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'birthday', 'born', 'description']
