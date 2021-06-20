from django.shortcuts import get_object_or_404, render,redirect
from .forms import WriteForm,CommentForm
from .models import Write,Comment
from django.contrib.auth.models import User

def community(request):
    user = request.user
    all_write = Write.objects.all()
    return render(request,'community.html',{'all_write':all_write,'user':user})

def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST,request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('community:community')
    else:
        create_form = WriteForm()
    return render(request,'create.html',{'create_form':create_form})

def detail(request,write_id):
    user= request.user
    my_write = get_object_or_404(Write, pk=write_id)
    comment_form = CommentForm()
    comments=Comment.objects.filter(post=write_id)
    return render(request,'detail.html',{'my_write':my_write,'comment_form':comment_form,'comments':comments, 'user':user})

def update(request,write_id):
    my_write = get_object_or_404(Write,pk=write_id)
    if request.method == "POST":
        update_form = WriteForm(request.POST,request.FILES,instance=my_write)
        if update_form.is_valid():
            update_form.save()
            return redirect('community:community')
    update_form = WriteForm(instance=my_write)
    return render(request,'update.html',{'update_form':update_form})

def delete(request,write_id):
    my_write = get_object_or_404(Write,pk=write_id)
    my_write.delete()
    return redirect('community:community')

def create_comment(request,write_id):
        if request.method == "POST":
            comment = CommentForm(request.POST)
            if comment.is_valid():
                form = comment.save(commit=False)
                user = request.user
                form.user = User.objects.get(id=user.id)
                form.post = Write.objects.get(id=write_id)
                form.save()
        return redirect('community:detail',write_id)

def delete_comment(request,write_id,comment_id):
    my_comment = get_object_or_404(Comment, id=comment_id)
    my_comment.delete()
    return redirect('community:detail',write_id)
      
        





# Create your views here.
