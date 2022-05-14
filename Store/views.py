from django.shortcuts import render,HttpResponse

from Store.forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'Store/index.html')


def get_user_feedback(request):

    form=ContactForm()
    if request.method.upper == 'POST':
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['superName'])
            print(form.cleaned_data['email'])
                        


    return render(request,"Store/form.html",{'form':form})

