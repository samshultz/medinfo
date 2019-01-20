from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.UserRegistrationView.as_view(), name="signup"),
    url(r'^$',views.user_detail_edit_view, 
        name='user_detail'),
    url(r'^users/list/$', views.UserListView.as_view(), name="user_list"),
]