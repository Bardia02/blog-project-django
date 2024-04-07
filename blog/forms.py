from django import forms
from django.core.validators import ValidationError
from .models import Message



class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=500,label="your message",required=False)
    name = forms.CharField(max_length=50,label='your name')
    birthday_year = forms.DateField(required=False, widget=forms.SelectDateWidget(years=['1381','1380','1382']))
    colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=[('blue','Blue'),('green','Green'),('black','Black')])
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same',code="name_text_same")
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            self.add_error('name','a can not be in name')
        return name

# class MessageForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea,label="enter your text")
#     title = forms.CharField(label="enter your title")
class  MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = ('title',"text","email")
        exclude = ("created_at",)
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control col-md-6 col-sm-12", "placeholder": "enter your title",
                "style": "max-width:300px;"
            })
            , "text": forms.TextInput(attrs={
                "class": "form-control"
            })
        }



