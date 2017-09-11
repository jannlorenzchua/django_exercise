# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Index(View):
    template_name = 'notes/index.html'
    
    def get_context_data(self):
        context = {}
        return context
        
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)