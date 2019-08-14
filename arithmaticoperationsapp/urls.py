from django.urls import path
from arithmaticoperationsapp import views
urlpatterns=[
path('input', views.input),
path('output', views.arithmatic),

]
