from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mainapp.models import Main
from mainapp.forms import PostForm

class IndexView(ListView):
  template_name = 'core/index.html'
  context_object_name = 'post_list'
  model = Main

class SinglePost(DetailView):
  template_name = 'core/single.html'
  model = Main
  context_object_name = 'post'

class PostView(ListView):
  template_name = 'core/posts.html'
  context_object_name = 'post_list'
  model = Main

class AddPost(CreateView):
  form_class = PostForm
  template_name = 'core/add.html'
  success_url = reverse_lazy('mainapp:posts')

class EditView(UpdateView):
  form_class = PostForm
  template_name = 'core/edit.html'
  pk_url_kwarg = 'pk'
  queryset = Main.objects.all()
  success_url = reverse_lazy('mainapp:posts')

class DeletePost(DeleteView):
  queryset = Main.objects.all()
  pk_url_kwarg = 'pk'
  template_name = 'core/confirm_delete.html'
  success_url = reverse_lazy('mainapp:posts')


