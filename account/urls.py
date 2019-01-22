from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signup/$', views.UserRegistrationView.as_view(), name="signup"),
    url(r'^$',views.user_detail_edit_view, 
        name='user_detail'),
    url(r'^users/list/$', views.UserListView.as_view(), name="user_list"),
    url(r'^user/statistics/$', views.statistical_details, name="user_statistics"),

    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name='logout'),
    
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, 
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete, name='password_reset_complete'),
]