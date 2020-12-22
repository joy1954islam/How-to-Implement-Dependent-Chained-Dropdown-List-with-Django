from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, City
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})



#this is function base django dependent dropdown
from django.http import JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
#
# from .forms import PersonForm
# from .models import Person, City
#
#
# def PersonCreateView(request):
#     form = PersonForm()
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_add')
#     return render(request, 'persons/home.html', {'form': form})
#
#
# def PersonUpdateView(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonForm(instance=person)
#     if request.method == 'POST':
#         form = PersonForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})
#
#
# # AJAX
# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
