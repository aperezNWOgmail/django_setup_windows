from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def home(request):
    return HttpResponse("Hello, Django!")


def my_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT TOP 10 * FROM accessLogs order by ID_COLUMN DESC")
        rows = cursor.fetchall()
    
    # Process rows or pass them to the template context
    context = {'rows': rows}
    return render(request, 'my_template.html', context)
