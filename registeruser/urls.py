from django.urls import path
from .views import RegisterUserView, ListUserRegisterView

# A namespace for the urls.
app_name = 'user'

# A list of url patterns.
urlpatterns = [
    path('registerUser/', RegisterUserView.as_view(), name='registerUser'),
    path('listUser/', ListUserRegisterView.as_view(), name='listUser')
]
