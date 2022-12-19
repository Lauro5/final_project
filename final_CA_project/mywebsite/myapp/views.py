from django.shortcuts import render, redirect
from .models import Blog, Blogcomment, Contact
from .forms import ContactForm, CreateBlogForm, CommentBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class blog_home(generic.ListView):
    model = Blog
    template_name = "myapp/blog_home.html"


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    all_comments = Blogcomment.objects.filter(blog = blog.id)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]

    form = CommentBlogForm()
    if request.method == "POST":
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been posted succesfully")
            return redirect("blog_detail" + blog.slug)
        else:
            form = CommentBlogForm()
    
    context = {
        'blog':blog,
        'all_blogs': all_blogs,
        'form': form,
        'all_comments': all_comments
    }
    return render(request, "myapp/blog_detail.html", context)

class blog_detail(generic.DetailView):
    model = Blog
    template_name = "myapp/blog_detail.html"

class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "myapp/contact_us.html"
    success_url = "/"
    success_message = "Your message has been submitted successfully, we will contact you soon"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the message again")
        return redirect('home')

class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "myapp/create_blog.html"
    login_url = 'login'
    success_url = "/"
    succes_message = "Your blog has been created"