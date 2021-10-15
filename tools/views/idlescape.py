from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from tools.forms import AugChanceForm
import math
from fractions import Fraction



def index(request):
    return HttpResponse("Hello, world. You're at the idlescape menu.")


def augment_calculator(request):
    if request.method == "POST":
        form = AugChanceForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            L = form.get("Enchanting")
            a = form.get("Augment")
            c = form.get("Chance")
            chance = (math.pow((0.9 + Fraction(int(math.sqrt(L * 1.5)), 200)), a)*100)+c
            return JsonResponse({'Result': chance})
    else:
        form = AugChanceForm()
    return render(request, 'tools/idlescape/augment_calculator.html', {'form': form})


