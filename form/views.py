from django.shortcuts import render
from .models import Question
from .forms import PostForm

def post_list(request):
    data = Question.objects.all()
    return render(request, 'form/form.html', {'form':data})



def post_detail(request,form_id):
    data = form.objects.get(id=form_id)
    return render(request,'form/detail.html',{'form':data})


def new_post(request):
    form = PostForm()
    return render(request,'form/new.html',{'form':form})

# Create your views here.
