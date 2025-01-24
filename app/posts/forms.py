from django import forms

from .models import Incoming, IncomingComment

class IncomingForm(forms.ModelForm):
    class Meta:
        model = Incoming
        fields = [
            "conf",
            "urgent",
            "received",
            "r_from",
            "note",
            "sender",
            "dated",
            "subject",
            "phone",
            "phone1",
            "file",
        ]
        
class IncomingCommentForm(forms.ModelForm):
    class Meta:
        model = IncomingComment
        fields = ["comment"]
        widgets = {
            "comments": forms.Textarea(attrs={"rows": 3, "cols": 30}),
        }