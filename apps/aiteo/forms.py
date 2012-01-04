from django import forms

from aiteo.models import Question, Response


class AskQuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AskQuestionForm, self).__init__(*args, **kwargs)

        # change a widget attribute:
        self.fields['content'].widget.attrs["rows"] = 5
    
    class Meta:
        model = Question
        fields = ["question", "content"]


class AddResponseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddResponseForm, self).__init__(*args, **kwargs)

        # change a widget attribute:
        self.fields['content'].widget.attrs["rows"] = 3
    
    class Meta:
        model = Response
        fields = ["content"]
