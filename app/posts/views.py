from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import IncomingForm, IncomingCommentForm
from .models import Incoming, IncomingComment, Outgoing, OutgoingComment


class IncomingListView(ListView):
    model = Incoming


class IncomingDetailView(DetailView):
    model = Incoming
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments_form"] = IncomingCommentForm
        return context


class IncomingUpdateView(UpdateView):
    model = Incoming
    form_class = IncomingForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class IncomingCreateView(CreateView):
    model = Incoming
    form_class = IncomingForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


def add_comment_view(request, slug):
    incoming = get_object_or_404(Incoming, slug=slug)

    if request.method == "POST":
        form = IncomingCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.incoming = incoming
            if request.user.is_authenticated:
                comment.created_by = request.user
                comment.updated_by = request.user
            comment.save()
            return redirect("incoming-detail", slug=slug)

    # If the form is not valid or the request method is not POST
    return render(
        request,
        "incoming/incoming_detail.html",
        {"incoming": incoming, "comment_form": form},
    )