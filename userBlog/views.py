from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MyBlogsDatabase, ContactDatabase
from django.contrib import messages

def indexHome(request):

        blogs = MyBlogsDatabase.objects.all()[::-1]
        oldBlogs = MyBlogsDatabase.objects.all()[0:3]
        context = {'blogs':blogs,'oldBlogs':oldBlogs,'title':'Blog-Page'}
        return render(request, 'userBlog/index.html', context)

@login_required
def blogPost(request, slug):
        blogPost_data = MyBlogsDatabase.objects.filter(slug=slug).first()
        PopBlogs = MyBlogsDatabase.objects.all()[0:3]
        context = {'blogPost':blogPost_data, 'popular':PopBlogs, 'title':blogPost_data.blogTitle}
        return render(request, 'userBlog/blogPosts.html', context)

@login_required
def contact(request):
        if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                message = request.POST['message']

                if request.user.username != username:
                        messages.error(request, "Username Does-not Match!!!")
                        return redirect('contactpage')
                
                if request.user.email != email:
                        messages.error(request, "Email Does-not Match!!!")
                        return redirect('contactpage')

                listen = ContactDatabase(username=username, email=email,message=message)
                listen.save()
                messages.success(request, 'Your Message Has Been Successfully Send...')
                return redirect('userBlogPage')
        
        return render(request, 'userBlog/contact.html',{'title':'Contact Page'})