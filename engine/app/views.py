from django.shortcuts import render,HttpResponse,get_object_or_404,get_list_or_404,redirect
from .models import *
from .forms import Productform
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import datafun,ProductSerializer
from rest_framework import viewsets
from rest_framework import generics

# Create your views here.
def home(request):
    products=product.objects.all()
    details=get_list_or_404(product)
    if request.method=='POST':
        form=Productform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            redirect('home.html')
    else:
        form=Productform()
    return render(request,'home.html',{'details':details,'form':form,'products':products})

@api_view(['GET'])
def Getdata(request):
    data={'name':'joker'}
    serializer=datafun(data=data)
    serializer.is_valid(raise_exception=True)  # Validate data
    return Response(serializer.data) 
def items(request,product_id):
    item=get_object_or_404(product,id=product_id)
    return render(request,'details.html',{'item':item})
class rout(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer