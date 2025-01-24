from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class UserAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_user

    def handle_no_permission(self):
        messages.info(self.request, "Your request could not be completed.")
        return redirect("/")
