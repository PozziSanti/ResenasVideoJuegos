from django.shortcuts import render, get_object_or_404, redirect
from apps.comment.models import Comment
from apps.comment.forms import CommentForm
from apps.review.models import Review
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  
            comment.review = review     
            comment.save()
            return redirect('review_detail', review_id=review.id)  #TODO Hacer una vista de detalle de review para redirigir a esa vista
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form, 'review': review})