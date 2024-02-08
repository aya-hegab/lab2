from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from products.models import Product

# products=[{'id':1, 'name':'iphone', 'src':'1.jpeg'},{'id':2, 'name':'redmi', 'src':'2.jpeg'}, {'id':3, 'name':'samsung', 'src':'3.jpeg'}]
# # Create your views here.
# def helloworld(request):
#   context = {}
#   context['products'] = products
#   return render(request, 'products/index.html', context)
# def helloworld2(request, pid):
#   myItem = list(filter(lambda t:t['id']==pid, products))  
#   if myItem:
#     return HttpResponse(f"hello world from products of {myItem}")
#   else:
#     return HttpResponse(f"item not found")
def productList(request):
  context={'products':Product.objects.all()}
  return render(request, 'products/index.html', context)


def productAddNew(request):
  if request.method == "POST":
    Product.objects.create(name=request.POST['pname']) 
    r=reverse('products')    
    return HttpResponseRedirect(r)
    # return HttpResponseRedirect('/products')
  return render(request, 'products/productAdd.html')


def productDetails(request, pid):
  obj1 = Product.objects.get(id=pid)
  context={'product':obj1}
  return render(request, 'products/productDetails.html', context)


def productDelete(request, pid):
  Product.objects.get(id=pid).delete()
  return HttpResponseRedirect('/products')