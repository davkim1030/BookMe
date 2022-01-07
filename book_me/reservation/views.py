from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponse
)
from django.shortcuts import render, get_object_or_404

from .models import User, Reservation
from .forms import UserForm, ReservationForm


def create_user(request):
    if request.method == 'POST':
        user_create_form = UserForm(request.POST)

        if user_create_form.is_valid():
            pass

        new_user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        return HttpResponse(new_user)

    elif request.method == 'GET':
        user_create_form = UserForm()
        return render(request, 'reservation/default_template.html', {'form': user_create_form})
    else:
        return HttpResponseNotAllowed

