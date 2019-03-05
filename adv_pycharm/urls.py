from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers
from polls import api_views

router = routers.DefaultRouter()
router.register('question', api_views.QuestionViewSet)
router.register('choice', api_views.ChoiceViewSet)
router.register('custom_question', api_views.CustomQuestionView, base_name="poll")

urlpatterns = [
    path('', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]

