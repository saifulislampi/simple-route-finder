# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (
        home,

    )


urlpatterns = [

    url(r'^$',home),
    # url(r'^all$', all_books, name='all_books'),


]
