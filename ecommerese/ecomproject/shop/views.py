from django.shortcuts import render,get_object_or_404
from. models import Product,Category
# Create your views here.
def home(request,slug_c=None):
    page_c=None
    products=None
    if slug_c !=None:
        page_c=get_object_or_404(Category, slug=slug_c)
        products=Product.objects.all().filter(category=page_c,available=True)
    else:
        products=Product.objects.all().filter(available=True)


    return render (request,'home.html',{'category':page_c,'product':products})


def base(request):
    return render(request,'base.html')



