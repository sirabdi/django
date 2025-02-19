from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def form_name_veiw(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # DO SOMETHING WHEN VALID
            print('Validation Success!')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])
            
    return render(request,'basic_app/form_page.html', {'form': form})