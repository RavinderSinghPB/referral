from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import SignUpForm
from .models import User, ReferCode
from .models import randCode
from .serializers import UserSerializer, ReferCodeSerializer


def index(request):
    return render(request, "app/index.html", )


def profile(request):
    context = {}
    if request.user.is_authenticated:
        referrer_code = request.user.user_refer_code
        no_of_referrals = User.objects.filter(used_refer_code=referrer_code).count()
        point_earned = no_of_referrals * 10
        context = {'no_of_referrals': no_of_referrals, 'point_earned_by_refer': point_earned, 'user': request.user, }

    return render(request, "app/profile.html", context)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], )
    def point_earn(self, request, pk=None):
        referrer_code = User.objects.get(pk=pk).user_refer_code
        no_of_referrals = User.objects.filter(used_refer_code=referrer_code).count()
        point_earned = no_of_referrals * 10

        result = {'no_of_referrals': no_of_referrals, 'point_earned_by_refer': point_earned}
        response = {'message': 'user refer code detail', 'result': result}
        return Response(response, status=status.HTTP_200_OK)


class ReferCodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReferCode.objects.all()
    serializer_class = ReferCodeSerializer

    @action(detail=True, methods=['get'], )
    def codeUsedBy(self, request, pk=None):
        code = ReferCode.objects.get(pk=pk)
        code_used_byUser = User.objects.filter(used_refer_code=code)
        users = {}

        for i in range(len(code_used_byUser)):
            users[i + 1] = {'username': code_used_byUser[i].username, 'email': code_used_byUser[i].email}

        return Response(users, status=status.HTTP_200_OK)


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():

            userForm = form.save(commit=False)
            userForm.user_refer_code = randCode()
            userForm.save()

            return redirect('/apilogin/')

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "app/signup.html", {"form": form, "msg": msg, "success": success})


def logout_view(request):
    logout(request)
    return render(request, "app/index.html", )
