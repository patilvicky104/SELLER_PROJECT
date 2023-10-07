from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, FormView

from django.shortcuts import render, redirect
from .models import AddCustomer, Contact
from .forms import BillForm, ContactForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

import pandas as pd
from django.http import JsonResponse

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Customer_List')


class Customer_List(LoginRequiredMixin, ListView):
    model = AddCustomer
    context_object_name = 'data'
    template_name = 'customer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = context['data'].filter(user=self.request.user)
        return context


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Customer_List')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Customer_List')
        return super(RegisterPage, self).get(*args, **kwargs)


class Customer_Form(CreateView):
    model = AddCustomer
    form_class = BillForm
    # fields = ["Name", "Phone", 'Buy_kgs', 'extra_kgs', 'Rate', 'Bill']

    success_url = reverse_lazy('Customer_List')
    template_name = 'BillForm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Customer_Form, self).form_valid(form)

    def get_initial(self):
        return {'Rate': 70,'Pending':'C'}


@login_required
def delete(request, pk):
    item = AddCustomer.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, "delete.html", {"item": item})


@login_required
def updateOrder(request, pk):
    order = AddCustomer.objects.get(id=pk)
    form = BillForm(instance=order)

    if request.method == 'POST':
        form = BillForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('Customer_List')

    context = {'form': form}
    return render(request, 'BillForm_update.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Mangos Required"
            body = {
                'Name': form.cleaned_data['Name'],
                'contact_number': str(form.cleaned_data['contact_number']),
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'patilvikrant104@gmail.com',
                          ['patilvicky104@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("Customer_List")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})

def Export_data_to_Excel(Request):
    objs = AddCustomer.objects.all()
    data= []
    for obj in objs:
        data.append({
            "Name": obj.Name,
            "Phone": obj.Phone,
            'Date': obj.Date,
            "Buy_kgs": obj.Buy_kgs,
            "extra_kgs": obj.extra_kgs,
            "Rate": obj.Rate,
            "Bill": obj.Bill,
            "Pending": obj.Pending,
        })
    pd.DataFrame(data).to_excel("Muktai Farm Customer list.xlsx")
    data1 = {
            "Download": "Successfully"
        }
    return JsonResponse(data1)


