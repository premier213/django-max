from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

monthly_challenge = {
    "january": "j index",
    "february": "f index",
    "march": "m index",
    "december": None
}


def index(request):
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challanges_int(request, month):
    m = list(monthly_challenge.keys())
    if month > len(m):
        return HttpResponseNotFound("this month not in range")
    redirect_month = m[month-1]
    reverse_redirect = reverse(redirect_month, args=[redirect_month])
    return HttpResponseRedirect(reverse_redirect)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()})
    except:
        return HttpResponseNotFound("this not supported")
