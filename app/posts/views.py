from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from users.user_permissions import CreatorAccessMixin

from .forms import IncomingCommentForm, IncomingForm
from .models import Incoming, IncomingComment, Outgoing, OutgoingComment


class IncomingListView(CreatorAccessMixin, ListView):
    model = Incoming
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()

        # Retrieve and apply filter parameters
        query = self.request.GET.get("q")
        urgent = self.request.GET.get("urgent")
        conf = self.request.GET.get("conf")

        if query:
            queryset = queryset.filter(
                Q(note__icontains=query)
                | Q(r_from__icontains=query)
                | Q(sender__icontains=query)
                | Q(subject__icontains=query)
                | Q(phone__icontains=query)
                | Q(phone__icontains=query)
            )
        if urgent == "1":
            queryset = queryset.filter(urgent=True)

        if conf == "1":
            queryset = queryset.filter(conf=True)
    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments_form"] = IncomingCommentForm

        # Preserve query parameters for pagination
        query_params = self.request.GET.copy()
        if "page" in query_params:
            query_params.pop(
                "page"
            )  # Remove 'page' from query parameters to prevent duplication
        context["query_params"] = urlencode(query_params)

        return context


class IncomingDetailView(CreatorAccessMixin, DetailView):
    model = Incoming


class IncomingUpdateView(CreatorAccessMixin, UpdateView):
    model = Incoming
    form_class = IncomingForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class IncomingCreateView(CreatorAccessMixin, CreateView):
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
