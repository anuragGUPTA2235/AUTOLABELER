import os
import cv2
from algorithm.object_detector import YOLOv7

# Initialize YOLOv7
yolov7 = YOLOv7()
yolov7.load('target.pt', classes='coco.yaml', device='gpu')  # use 'gpu' for CUDA GPU inference

# Specify the directory containing your images
image_dir = 'labeller'

# Create a directory to store the output text files
output_dir = 'annotations'
os.makedirs(output_dir, exist_ok=True)

# Iterate over all the image files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.png', '.jpeg')):  # Filter by image file extensions
        image_path = os.path.join(image_dir, filename)

        # Load the image
        image = cv2.imread(image_path)
        height, width, _ = image.shape

        # Detect objects
        detections = yolov7.detect(image)

        # Create a text file for each image
        output_filename = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(output_dir, output_filename)

        # Write the detections to the text file in the specified format
        with open(output_path, 'w') as file:
            for detection in detections:
                x_center = (detection['x'] + detection['width'] / 2) / width
                y_center = (detection['y'] + detection['height'] / 2) / height
                w = detection['width'] / width
                h = detection['height'] / height
                file.write(f'1 {x_center} {y_center} {w} {h}\n')

print("Detection and saving complete.")

