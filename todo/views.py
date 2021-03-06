from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect

from django.shortcuts import redirect, render, get_object_or_404

from todo.models import Task

from django.urls import reverse

from todo.forms import RegistrationForm, LoginForm, TaskForm, EditForm

from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('todo:user_page', args=(request.user.id,)))
    
    tasks = None
    obj_list = None
    
    user = request.user
    task_form = TaskForm()
    if request.method == 'POST':
        try:

            title = request.POST['text']
            date = request.POST['date']
            email = request.POST['email']
            print(date)
            task_obj = Task(title=title, when_to_do=date, email=email)
            for task in Task.objects.all():
                if title == task.title and (email == task.email or task.email == '' or task.email == None):
                    return redirect(reverse('todo:index'))
            task_obj.save()
        except:
            messages.error(request, f"There was error in submitting your task, enter date field.")
            return redirect(reverse('todo:index'))
        else:
        # check if this data already exist for this email
 
            tasks = Task.objects.all().filter(email=email)[::-1]
            obj_list = tasks[:5]

    return render(request, 'todo/index.html', {
        'tasks':obj_list,
        'task_form':task_form,
    })

def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('todo:index'))
 
    login_form = LoginForm()
    if request.method == 'POST':
        try:
            login_form = RegistrationForm(request.POST)

            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            
            print(user.id)
            if user is not None:
                login(request, user)

                
        except:
            messages.info(request, f"Please fill the form")
            return HttpResponseRedirect(reverse('todo:login_page'))
        else:
        
            #get user from User model 
            user_obj = User.objects.get(username=user.id)

            all_task = Task.objects.all()
            for task in all_task:
                if task.user_id == None and task.email == user_obj.email:
                    
                    task_object = Task.objects.get(pk=task.id)
                    task_object.user_id = user_obj.id
                    task_object.save()
            return HttpResponseRedirect(reverse('todo:user_page', args=(user_obj.id,)))

    return render(request, 'todo/login.html', {
        'login_form':login_form,
    })


def register_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('todo:index'))
    register_form = RegistrationForm()

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
# This should be ran by a signal
            username = register_form.cleaned_data['username']

            email = register_form.cleaned_data['email']
        # Get user records with the register email and username
        # fetch all task, loop through task to find if this user has a user_id == None with this email.
        # get task user_id and bind with this reg. user id
        # !!!! important: when updating a model object always use the .save() with the record_object itself.
            this_user = User.objects.get(username=username, email=email)

            all_task = Task.objects.all()
            
            for task in all_task:
                if task.user_id == None and task.email == this_user.email:
                    # print(task.id, task.user_id, this_user.id)
                    
                    task_object = Task.objects.get(pk=task.id)
                    # print(task_object)
                    task_object.user_id = this_user.id
                    task_object.save()
                    messages.success(request, f"Successfully created {username}, Enter credentals to Login.")
            messages.success(request, f"Successfully created {username}, Enter credentals to Login.")    
            return redirect(reverse('todo:login_page'))
                    
    return render(request, 'todo/register.html', {

        'register_form':register_form,

    })


def user_page(request, pk):
    if not request.user.is_authenticated:
        return redirect(reverse('todo:login_page'))
    user_obj = get_object_or_404(User, pk=pk)

    if request.method == "POST":

        try:
            title = request.POST['text']
            date = request.POST['date']
            email = user_obj.email

            obj = Task(user=request.user, title=title, when_to_do=date, email=email)
            obj.save()
        except:
            messages.info(request, f"Please fill the fields")
            return redirect(reverse('todo:user_page', args=(pk,)))
        else:
            return redirect(reverse('todo:user_page', args=(pk,)))


    task = user_obj.task_set.all().order_by('-created')
    return render(request, 'todo/user_page.html', {
        'user_obj':user_obj,
        'tasks':task,
    })

def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect(reverse('todo:login_page'))
    task = get_object_or_404(Task, pk=pk)
    edit_form = EditForm(instance=task)

    if request.method == 'POST':
        edit_form = EditForm(request.POST, instance=task)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('todo:user_page', args=(request.user.id, )))
    return render(request, 'todo/edit.html', {
        'form': edit_form,
        'task':task,
    })

def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect(reverse('todo:login_page'))

    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:user_page', args=(request.user.id,)))
    return render(request, 'todo/delete.html', {
        'task':task,
    })

def logout_handler(request):
    logout(request)
    return redirect(reverse('todo:index'))