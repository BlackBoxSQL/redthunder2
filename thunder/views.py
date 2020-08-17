from django.shortcuts import render
from .models import Joma, Club_Members
# Create your views here.
from django.db.models import Sum
from django.http import Http404


def homepage(request):
    context = {
        "totalmembers": Club_Members.objects.count(),
        "membersname": Club_Members.objects.all(),
        "jomadetails": Joma.objects.all(),
        "totalsavings": Joma.objects.aggregate(totalsavings=Sum('amount'))['totalsavings'],
    }
    return render(request, 'thunder/index.html', context)


def memberdetails(request, member_id):
    try:
        totalamount = Joma.objects.filter(
            member_id=member_id).aggregate(totalamount=Sum('amount'))['totalamount']
    except Joma.DoesNotExist:
        raise Http404("Data does not exist.")
    context = {
        "totalamount": totalamount,
        "totaldetails": Joma.objects.all().filter(member_id=member_id),
    }
    return render(request, 'thunder/details.html', context)
