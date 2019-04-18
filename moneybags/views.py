from django.shortcuts import render
from moneybags.models import Bills
from .forms import NewBillForm
# Create your views here.


def index(request):

    new_bill_form = NewBillForm()

    if request.method == "POST":
        newbill = Bills.objects.create(
            name=request.POST.get('name'),
            zero_interest_date=request.POST.get('interest_rate_date'),
            start_amount=request.POST.get('start_amount')
            )
        newbill.save()

    bills = Bills.objects.all()
    context = {
        "bills": bills,
        "new_bill_form": new_bill_form,
    }

    return render(request, 'moneybags/home.html', context=context)
