from django.shortcuts import render
from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
# from .service import send
from .tasks import send_message_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/index.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_message_email.delay(user_email=form.instance.email, user_name=form.instance.name)
        return super().form_valid(form)

