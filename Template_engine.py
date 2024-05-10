#!/usr/bin/env bash

def render(template_name, context, request=None):
    # Step 1: Load Template
    with open(template_name, 'r') as file:
        template_content = file.read()

    # Step 2: Replace Template Variables
    for key, value in context.items():
        template_content = template_content.replace("{{" + key + "}}", str(value))

    # Step 3: Handle Special Template Tags
    template_content = handle_special_tags(template_content, context, request)

    # Step 4: Return Rendered HTML
    return template_content

def handle_special_tags(template_content, context, request=None):
    # Handle special template tags like {{ video }}, {{ image }}, etc.
    # For simplicity, let's just handle a few tags as examples

    # Handle {{ video }}
    if "{{ video }}" in template_content:
        video_url = context.get("video", "")
        video_tag = f"<video src='{video_url}' controls></video>"
        template_content = template_content.replace("{{ video }}", video_tag)

    # Handle {{ image }}
    if "{{ image }}" in template_content:
        image_url = context.get("image", "")
        image_tag = f"<img src='{image_url}' alt='Image'>"
        template_content = template_content.replace("{{ image }}", image_tag)

    # Handle {{ form }}
    if "{{ form }}" in template_content and request:
        # Assume we have a Django form object in the context
        form = context.get("form")
        form_html = str(form)
        template_content = template_content.replace("{{ form }}", form_html)

    # Other special template tags can be handled similarly

    return template_content

# Example usage:
context = {
    'message': 'This is a sample message.',
    'image': 'example.jpg',
    'video': 'example.mp4',
    'form': '<input type="text" name="username" placeholder="Enter your username">'
}
rendered_html = render('index.html', context)
print(rendered_html)

