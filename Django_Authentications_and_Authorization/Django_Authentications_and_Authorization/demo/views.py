from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model, authenticate, login, logout
from random import randint
from django.contrib.auth.decorators import login_required

UserModel = get_user_model()


def index(request):
    current_user = UserModel.objects.filter(username=request.user.username).all()
    suffix = randint(0, 1000)

    user_data = {
        'username': f'user_{suffix}',
        'password': '1234QAWSe',
    }
    new_user = UserModel.objects.create_user(**user_data)

    context = {
        'current_user': current_user,
        'has_permission': request.user.has_perm('auth.view_user'),
        'users_count': UserModel.objects.all().count(),
    }

    authenticate(request)
    print(request.user)
    return render(request, 'index.html', context)


def login_user(request):

    # Authentication
    current_user = authenticate(
        username='user_915',
        password='1234QAWSe',
    )

    # Authorization
    # request.user = user
    login(request=request, user=current_user)
    print(f'Authenticated user: {current_user}')
    return redirect('index')


@login_required()
def logout_user(request):
    logout(request=request)
    return redirect('index')

