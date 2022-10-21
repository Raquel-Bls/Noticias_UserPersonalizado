from django.urls import path
from .views import SignUpView, homePageview

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('', homePageview.as_view(), name='home'),
]
