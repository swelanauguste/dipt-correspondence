from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class CreatorAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_creator

    def handle_no_permission(self):
        messages.info(self.request, "Your request could not be completed.")
        return redirect("login")

class AdminAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_creator

    def handle_no_permission(self):
        messages.info(self.request, "Your request could not be completed.")
        return redirect("login")
