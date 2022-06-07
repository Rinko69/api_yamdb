import uuid

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
# from django.contrib import messages
# from django.contrib.sites.models import Site
# from django.contrib.sites.requests import RequestSite
# from django.db import IntegrityError
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.views.generic import CreateView
# from django.views.generic.base import RedirectView
# from rest_framework import mixins, request
# from django.urls import reverse_lazy, reverse, settings

from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer,
                          GenreSerializer, TitleSerializer,
                          TitlePostSerializer,
                          )
from .models import Category, Genre, Title
# from .forms import CreationForm
# from .models import User, RegistrationProfile


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('category__slug', 'genre__slug', 'name', 'year')
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH',):
            return TitlePostSerializer
        return TitleSerializer
