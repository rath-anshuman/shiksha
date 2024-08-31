from django.urls import path,include


from .views import login_user,logout_user
urlpatterns = [
    # path('register/',register_user),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
