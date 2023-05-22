from django.shortcuts import render
from .models import CurrencyPair, CurrencyStory


def rand_vs_dollar(request):
    currency_pairs = CurrencyPair.objects.all()
    rand_values = [pair.rand for pair in currency_pairs]
    dollar_values = [pair.dollar for pair in currency_pairs]
    return render(request, 'currency_analysis/rand_vs_dollar.html', {'rand_values': rand_values, 'dollar_values': dollar_values})

def dollar_to_aud(request):
    currency_pairs = CurrencyPair.objects.all()
    dollar_values = [pair.dollar for pair in currency_pairs]
    aud_values = [pair.australian_dollar for pair in currency_pairs]
    return render(request, 'currency_analysis/dollar_to_aud.html', {'dollar_values': dollar_values, 'aud_values': aud_values})