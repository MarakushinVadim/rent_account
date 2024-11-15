from django.urls import path

from rent.views import BaseView

app_name = 'rent'

urlpatterns = [
    path('', BaseView.as_view(), name='base')
]