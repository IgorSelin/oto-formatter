import cv2
import numpy as np
from PIL import Image

def extract_points_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    points = []
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if 3 < w < 15 and 3 < h < 15:
            points.append((x, y))
    return points

def convert_points_to_nhax(points, output_path):
    with open(output_path, 'w') as f:
        f.write("NHAX_FORMAT\n")
        for x, y in points:
            f.write(f"{x},{y}\n") 