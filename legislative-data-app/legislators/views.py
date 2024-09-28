from django.shortcuts import render
import csv
import os
from django.conf import settings

def load_csv_data(file_name):
    """Load data from a CSV file into a list of dictionaries."""
    file_path = os.path.join(settings.BASE_DIR, 'data', file_name)
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
    return data

def legislators_view(request):
    """View to display legislators and their voting statistics."""

    legislators = load_csv_data('legislators.csv')
    bills = load_csv_data('bills.csv')
    vote_results = load_csv_data('vote_results.csv')
    votes = load_csv_data('votes.csv')

    legislator_stats = {legislator['id']: {
        'name': legislator['name'],
        'supported': 0,
        'opposed': 0
    } for legislator in legislators}

    bill_stats = {bill['id']: {
        'title': bill['title'],
        'primary_sponsor': '',
        'supporters': 0,
        'opposers': 0
    } for bill in bills}

    for bill in bills:
        sponsor_id = bill['sponsor_id']
        for legislator in legislators:
            if legislator['id'] == sponsor_id:
                bill_stats[bill['id']]['primary_sponsor'] = legislator['name']
                break

    vote_to_bill_map = {vote['id']: vote['bill_id'] for vote in votes}

    for result in vote_results:
        legislator_id = result['legislator_id']
        vote_id = result['vote_id']
        vote_type = result['vote_type']

        bill_id = vote_to_bill_map.get(vote_id)

        print(f"Processing vote: Legislator ID: {legislator_id}, Bill ID: {bill_id}, Vote Type: {vote_type}")

        if legislator_id in legislator_stats:
            if vote_type == '1':
                legislator_stats[legislator_id]['supported'] += 1
                if bill_id in bill_stats:
                    bill_stats[bill_id]['supporters'] += 1
            elif vote_type == '2':
                legislator_stats[legislator_id]['opposed'] += 1
                if bill_id in bill_stats:
                    bill_stats[bill_id]['opposers'] += 1

    print("Legislator Stats:", legislator_stats)
    print("Bill Stats:", bill_stats)

    return render(request, 'legislators.html', {
        'legislator_stats': legislator_stats,
        'bill_stats': bill_stats,
    })
