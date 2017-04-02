from django.views.generic import CreateView
from django.urls import reverse

from .forms import CommentForm
from .models import Comment
from core.models import User
from blogs.models import Post


class CommentFormView(CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'blogs/one_post.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = User.objects.get(pk=self.request.user.pk)
        comment.post = Post.objects.get(pk=self.request.POST.get('post_id'))
        comment.save()
        return super(CommentFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blogs:one_post', kwargs={'pk': self.object.post.pk})
