from django.shortcuts import render, get_object_or_404
from .models import Activities as Act
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils.decorators import method_decorator



def home(request):
    context = {
        'Act': Act.objects.all()
    }
    return render(request,'tasks/home.html',context)

class PostListView(ListView):
    model=Act
    template_name='tasks/home.html'
    context_object_name='Act'
    ordering=['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model=Act
    template_name='tasks/user_activities.html'
    context_object_name='Act'
    ordering=['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Act.objects.filter(author=user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Act
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Act
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Act
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False

def about(request):
    return render(request,'tasks/about.html')

@login_required
def required_task(request):
    context={
        'Act': Act.objects.all()
    }
    return render(request,'tasks/task.html',context)

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Act
