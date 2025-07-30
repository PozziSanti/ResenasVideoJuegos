from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.review.models import Review
from apps.favorite.models import Favorite

@login_required
def toggle_favorite(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, review=review)

    if not created:
        favorite.delete()

    return redirect('detalle_review', review_id=review.id)