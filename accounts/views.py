from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class RegisterAPIView(APIView):

    def post(self, request):  # noqa
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        username = request.GET.get('username')
        password = request.GET.get('password')
        password_confirm = request.GET.get('password_confirm')

        if password == password_confirm:
            if User.objects.filter(email=email).exists():
                return Response({'Success': False, 'message': 'Этот адрес электронной почты уже существует'},
                                status=400)
            if User.objects.filter(username=username).exists():
                return Response({'Success': False, 'message': 'Такое имя пользователя уже существует!'}, status=400)
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )
                return Response({'success': True, 'message': 'Успешная регистрация'})
        else:
            return Response({'Success': False, 'message': 'Неверный пароль!'})
