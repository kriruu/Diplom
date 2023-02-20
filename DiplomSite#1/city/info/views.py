from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView





# class BackVideo():
#     def get_context_data(request): #httprequest

#         mydata = VideoBackHome.objects.all().values()
#         template = loader.get_template('city/index.html')
#         context = {
#             'mymembers': mydata,
#         }
#         # return render (request,'city/index.html', {'title': a}) 
#         return HttpResponse(template.render(context, request))

    
def about(request): #httprequest
    return render (request,'city/about.html',{'title':'about'})  
    

# class BackVideo(ListView):
#     model = InfoForAll
#     template_name = 'city/index.html'
#     context_object_name = 'video'
#     video = VideoBackHome.objects.all().values()
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['video']
#         return context
        
#     def get_queryset(self):
#         return InfoForAll.objects()

class InfoHome(ListView):
    model = InfoForAll
    template_name = 'city/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        context['video'] = VideoBackHome.objects.all()
        

        return context
        
    def get_queryset(self):
        return InfoForAll.objects.filter(is_published=True, cat=1).order_by('-pk')[:3]

    


class ShowPost(DetailView):
    model = InfoForAll
    template_name = 'city/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        # context['menu'] = menu
        return context

class InfoCategory(ListView):
    model = InfoForAll
    template_name = 'city/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return InfoForAll.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
