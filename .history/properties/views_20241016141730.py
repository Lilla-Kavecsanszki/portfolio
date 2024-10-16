from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Lower
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from .decorators import superuser_required
from .forms import PropertyForm, PropertyImageFormSet, PropertyVideoFormSet
from .models import Property, PropertyImage, PropertyVideo