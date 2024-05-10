# views.py

import os
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

def create_html_file(request):
    # Process the data and generate profile information
    profile_info = {
        'name': 'John Doe',
        'age': 30,
        # Add more profile information as needed
    }

    # Render HTML template with profile information
    rendered_html = render_to_string('profile_template.html', {'profile': profile_info})

    # Write rendered HTML to a new file
    file_path = '/path/to/new_file.html'  # Change to your desired file path
    with open(file_path, 'w') as file:
        file.write(rendered_html)

    # Return the file path
    return JsonResponse({'file_path': file_path})
