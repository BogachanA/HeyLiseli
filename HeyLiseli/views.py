from django.shortcuts import render, redirect
from catalog.forms import loginForm,social_auth_complete
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect

def home(request):
    if not request.session.get('has_session'):
        request.session['has_session'] = True

    return render(request, 'base.html')


def loginView(request):
    if request.user.is_authenticated:

        # -Todo: redirect to profile page instead of where the user came from
        referer = request.META.get('HTTP_REFERER')
        if referer:
            print(referer)
            return HttpResponseRedirect(referer)
        else:
            return HttpResponseRedirect("/")

    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    pass

    else:
        form = loginForm()

    context = {'form': form}

    return render(request, 'registration/login.html', context)


def social_auth_extras(request):
    if request.method == "POST":
        method_type="post"
        form=social_auth_complete(request.POST)
        if form.is_valid():
            user=request.user
            user.email=form.cleaned_data['email']
            user.grade=form.cleaned_data['grade']
            user.lise=form.cleaned_data['lise']
            user.save()
            return HttpResponseRedirect("/accounts/activate/complete/")
    else:
        method_type="get"
        form=social_auth_complete()
    context={'form':form,'method':method_type,}
    return render(request,'registration/social_register_extras.html',context)



'''
For deleting all user sessions at once (For example after changing password)

def delete_user_sessions(user):
    user_sessions = UserSession.objects.filter(user = user)
    for user_session in user_sessions:
        user_session.session.delete()

'''