from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Incoming, IncomingComment, Outgoing, OutgoingComment


class IncomingListView(ListView):
    model = Incoming


class IncomingDetailView(DetailView):
    model = Incoming


class IncomingUpdateView(UpdateView):
    model = Incoming
    fields = "__all__"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class IncomingCreateView(CreateView):
    model = Incoming
    fields = "__all__"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
