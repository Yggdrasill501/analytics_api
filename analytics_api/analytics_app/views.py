from django.shortcuts import render

import os
from django.conf import settings
from django.http import JsonResponse
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authentication and Google Analytics API setup
def initialize_analyticsreporting():
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_ANALYTICS_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics

def get_report(request):
    analytics = initialize_analyticsreporting()
    
    # Example request body
    report_request = {
        'reportRequests': [
            {
                'viewId': 'YOUR_VIEW_ID',
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:country'}]
            }
        ]
    }

    response = analytics.reports().batchGet(body=report_request).execute()
    
    return JsonResponse(response)

# Example view to get data
def sessions_by_country(request):
    analytics = initialize_analyticsreporting()
    
    report_request = {
        'reportRequests': [
            {
                'viewId': 'YOUR_VIEW_ID',
                'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:country'}]
            }
        ]
    }
    
    response = analytics.reports().batchGet(body=report_request).execute()
    data = response['reports'][0]['data']['rows']
    
    result = [{'country': row['dimensions'][0], 'sessions': row['metrics'][0]['values'][0]} for row in data]
    
    return JsonResponse(result, safe=False)
