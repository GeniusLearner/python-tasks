from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

def send_message(name, message):
    #code for actually sending the message goes here

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def contact_view(request):
    # The request method 'POST' indicates that the form was submitted
    if request.method == 'POST':
        #Create a form instance with the submitted data
        form = ContactForm(request.POST)
        # Create a form instance with the submitted data
        form = ContactForm(request.POST)
        # validate the form
        if form.is_valid():
            # if the form is valid, perform some kind of
            #operation, for example sending a message
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['message']
            )
            # After the operation was successful,
            # redirect to some other page
            return redirect('/success/')
        else:
            # Create an empty form instance
            form = ContactForm()

        return render(request, 'contact_form.html', {'form': form})
