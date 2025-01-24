from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "change-password/",
        views.change_password_change_view,
        name="change-password",
    ),
    path(
        "change-password-done/",
        views.UserPasswordChangeDoneView.as_view(),
        name="change_password_done",
    ),
    path(
        "password-reset/", views.UserPasswordResetView.as_view(), name="password-reset"
    ),
    path("forgot-password/", views.forgot_password_view, name="forgot-password"),
    path(
        "reset-password/<uidb64>/<token>/",
        views.reset_password_view,
        name="reset-password",
    ),
    # path(
    #     "password-reset-done/",
    #     views.UserPasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password-reset-confirm/<uidb64>/<token>/",
    #     views.UserPasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    path(
        "password-reset-complete/",
        views.UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("user-detail/", views.user_detail, name="user-detail"),
    path("user-update/", views.user_update, name="user-update"),
    path("register/", views.user_registration_view, name="register"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path(
        "user/get-user-detail/<slug:slug>/",
        views.get_user_detail,
        name="get-user-detail",
    ),
    path("user-list/", views.UserListView.as_view(), name="user-list"),
]