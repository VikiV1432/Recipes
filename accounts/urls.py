from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignInPage, SignUpPage, ProfilePage, EditProfilePage

urlpatterns = [
    path("logout/",LogoutView.as_view(next_page='home'), name='logout'),
    path("sign-in/", SignInPage.as_view(), name="sign-in"),
    path("sign-up/",SignUpPage.as_view(),name='sign-up'),
    path("profile/<str:username>",ProfilePage.as_view(),name='profile'),
    path("edit-profile/",EditProfilePage.as_view(),name='edit-profile')
]
