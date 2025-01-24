from django.urls import path

from . import views

urlpatterns = [
    path("", views.IncomingListView.as_view(), name="incoming-list"),
    path(
        "incoming/detail/<slug:slug>/",
        views.IncomingDetailView.as_view(),
        name="incoming-detail",
    ),
    path(
        "incoming//update<slug:slug>/",
        views.IncomingUpdateView.as_view(),
        name="incoming-update",
    ),
    path(
        "incoming/create/", views.IncomingCreateView.as_view(), name="incoming-create"
    ),
    path(
        "incoming-comment/<slug:slug>/",
        views.add_comment_view,
        name="incoming-add-comment",
    ),
]
