from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
    path('(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #path('^(?P<pk>[0-9]+)/vote/$', views.SwitchboardView.as_view(), name="vote_result"),
]
