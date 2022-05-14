import imp
from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    superName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    verify_email = forms.EmailField(max_length=40)
    message = forms.CharField(widget=forms.Textarea)

    human_detection = forms.CharField(required=False,widget=forms.HiddenInput)


    def check_human(self):
        var = self.cleaned_data['human_detection']
        if var:
            raise forms.ValidationError('not good')
        print(var)    
        return var    


