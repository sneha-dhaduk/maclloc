from django.shortcuts import render
from .models import macllocmedia,studentreview
from .forms import studentForm
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


# Create your views here.
class home(View):
    s=studentreview.objects.all()
    m=macllocmedia.objects.all()[:4]
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        if search != None:
            self.m=macllocmedia.objects.filter(contain__icontains=search)
        data={
            'rec':self.m,
            'rec1':self.s,
        }
        return render(request,'maclloc.html',data)
    
    # def post(self, request, *args, **kwargs):
    #     form=studentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return render(request,'maclloc.html')

    
# def maclloc(request):
    
# def detail(request,id):
#     det=macllocmedia.objects.get(contain=id)
#     return render(request,'result.html',{'det':det})


class detail(DetailView):
    model=macllocmedia
    template_name='result.html' # demo/templates/modelname_detail.html
    # context_object_name='det'  # default name is object 

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     string=self.get_object().contain1
    #     list = string.split("$")
    #     context['list']=list  
    #     return context
    
class contact(View):
    def get(self, request, *args, **kwargs):
        form=studentForm()
        return render(request,'contact.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'contact.html',{'form':form})
    
# class home(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'maclloc.html')
class college_course(View):
    def get(self, request, *args, **kwargs):
        return render(request,'college_course.html')
class activities(View):
    def get(self, request, *args, **kwargs):
        return render(request,'activities.html')
class about_us(View):
    def get(self, request, *args, **kwargs):
        return render(request,'about_us.html')
class blog(View):
    def get(self, request, *args, **kwargs):
        return render(request,'blog.html')
# class course(View):
#     def get(self, request, *args, **kwargs):
#         data=macllocmedia.objects.all()
#         return render(request,'course.html',{'rec':data})
    
class course(ListView):
    model=macllocmedia
    template_name='course.html'
    context_object_name='rec' # default name is object_list