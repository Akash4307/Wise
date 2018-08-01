from django.shortcuts import render
from .models import PdfInfo
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list import ListView
from .forms import UserForm


class PdfView(generic.ListView):
    template_name = 'Ebooks/pdfview.html'

    def get_queryset(self):
        return PdfInfo.objects.all().order_by('-created')


class EbookDetail(generic.DetailView):
    model = PdfInfo
    template_name = 'Ebooks/ebookdetail.html'

def sellebooks(request):
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()


        context = {
            "form": form,
         


    }
        return render (request, 'Ebooks/sellebooks.html', context)