from django.urls import path

from . import views

urlpatterns = [
    path("", views.IncomingListView.as_view(), name="incoming-list"),
    path(
        "incoming/<slug:slug>/",
        views.IncomingDetailView.as_view(),
        name="incoming-detail",
    ),
    path(
        "incoming/<slug:slug>/update/",
        views.IncomingUpdateView.as_view(),
        name="incoming-update",
    ),
    path(
        "incoming/create/", views.IncomingCreateView.as_view(), name="incoming-create"
    ),
]
