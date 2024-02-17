import os
from django.conf import settings
from django.shortcuts import render
import cv2
import numpy as np

def sharpen_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Save the uploaded image locally
        uploaded_image = request.FILES['image']
        uploaded_image_path = os.path.join(settings.BASE_DIR, 'static/assets/images', 'uploaded_image.jpg')
        with open(uploaded_image_path, 'wb') as f:
            for chunk in uploaded_image.chunks():
                f.write(chunk)

        # Read the uploaded image
        original_image = cv2.imread(uploaded_image_path)

        # Create the sharpening kernel
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        # Sharpen the image
        sharpened_image = cv2.filter2D(original_image, -1, kernel)

        # Save the sharpened image
        sharpened_image_path = os.path.join(settings.BASE_DIR, 'static/assets/images', 'sharpened_image.jpg')
        cv2.imwrite(sharpened_image_path, sharpened_image)

        return render(request, 'sharpened_image.html', {'uploaded_image_path': '/static/assets/images/uploaded_image.jpg', 'sharpened_image_path': '/static/assets/images/sharpened_image.jpg'})
    return render(request, 'upload_image.html')
