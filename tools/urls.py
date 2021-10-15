from django.urls import re_path
from .views import main
from .views import idlescape

app_name = "tools"
urlpatterns = [
    re_path(r'^$', main.index, name='index'),
    re_path(r'^idlescape/$', idlescape.index, name="index"),
    re_path(r'^idlescape/enchant/augment/calculator$', idlescape.augment_calculator, name="augment_calculator")
]