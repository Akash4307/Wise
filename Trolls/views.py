from django.shortcuts import render
from .models import UserInfo
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list import ListView
from .forms import UserForm


    

class Facebook(generic.ListView):
    template_name = 'Trolls/facebook.html'
    model = UserInfo




def DetailView(request):
    query = request.GET.get('q')
    result = UserInfo.objects.filter(UserBookName__startswith = query).order_by('-created')
    context = {
        'query': query,
        'object_list': result,
        }
    return render(request, 'Trolls/detail.html', context)
    



def sell(request):
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()


        context = {
            "form": form,
         

    }
        return render (request, 'Trolls/sell.html', context)


class buy(generic.ListView):
    template_name = 'Trolls/buy.html'

    def get_queryset(self):
        return UserInfo.objects.all().order_by('-created')


class BookDetail(generic.DetailView):
    model = UserInfo
    template_name = 'Trolls/bookdetail.html'


def UserCreate(request):
    form = UserForm()
    context = {
        "form": form,
         

    }
    return render (request, 'Trolls/user_form.html', context)



