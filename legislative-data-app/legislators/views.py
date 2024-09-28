from django.shortcuts import render
from django.db.models import Count, Q
from .models import Legislator, Bill, Vote

def legislators_view(request):
    """View to display legislators and their voting statistics."""

    legislator_stats = (
        Legislator.objects.annotate(
            supported=Count('vote', filter=Q(vote__vote_type='1')),
            opposed=Count('vote', filter=Q(vote__vote_type='2'))
        ).values('id', 'name', 'supported', 'opposed')
    )

    bill_stats = (
        Bill.objects.annotate(
            supporters=Count('vote', filter=Q(vote__vote_type='1')),
            opposers=Count('vote', filter=Q(vote__vote_type='2'))
        ).values('id', 'title', 'sponsor__name', 'supporters', 'opposers')
    )

    print("Legislator Stats:", list(legislator_stats))
    print("Bill Stats:", list(bill_stats))

    return render(request, 'legislators.html', {
        'legislator_stats': legislator_stats,
        'bill_stats': bill_stats,
    })
