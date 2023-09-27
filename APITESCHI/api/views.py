from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Signin(APIView):
    template_name="signin.html"
    def get(self,request):
        print('Enviando formulario')
        return render(request,self.template_name)
    def post(self,request):
        print('Obteniendo datos')
        return render(request,self.template_name)
    
def signin(request):

    if request.method == 'GET':
        print('Enviando formulario')
    else:
        print('Obteniendo datos')

    return render(request, 'signin.html', {

    })

class Signup(APIView):
    template_name="signup.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Error(APIView):
    template_name="error-404.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Icon(APIView):
    template_name="icon-material.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Pages(APIView):
    template_name="pages-profile.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Starter(APIView):
    template_name="starter-kit.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Table(APIView):
    template_name="table-basic.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)
