from django.shortcuts import render
from educat.models import Type, Module


# Create your views here.
def index(request):
	categories = Type.objects.all()
	context = {
		'categories': categories
	}

	return render(request, 'educat/base.html', context)


# Create your views here.
def category(request):
	categories = Type.objects.all()
	context = {
		'categories': categories
	}

	return render(request, 'educat/base1.html', context)



def search(request, *args, **kwargs):
	query = request.GET.get('query')
	resultats = Module.objects.filter(name__icontains=query)
	context = {
        'resultat': resultats,
	}
	return render(request,'educat/base.html', context, name='search')



def moduledetails(request):
	id = request.GET.get(query)
	module = Module.objects.filter(pk=id)
	context = {
		'module': module
	}
	return render(request, 'educat/base2.html', context)


def home(request):
	categories = Type.objects.all()
	context = {
		'categories': categories
	}

	return render(request, 'educat/base.html', context)
