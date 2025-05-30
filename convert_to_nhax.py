from PIL import Image
import numpy as np
import io

def extract_points_from_image(image_data):
    # Open the image from bytes
    img = Image.open(io.BytesIO(image_data))
    # Convert to grayscale
    img = img.convert('L')
    # Convert to numpy array
    img_array = np.array(img)
    # Threshold the image
    threshold = 200
    binary = img_array < threshold
    
    # Find points (pixels that are True in binary image)
    points = []
    height, width = binary.shape
    for y in range(height):
        for x in range(width):
            if binary[y, x]:
                # Check if this is a local maximum (simple blob detection)
                is_local_max = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < height and 0 <= nx < width:
                            if binary[ny, nx] and img_array[ny, nx] < img_array[y, x]:
                                is_local_max = False
                                break
                    if not is_local_max:
                        break
                if is_local_max:
                    points.append((x, y))
    
    return points

def convert_points_to_nhax(points):
    # Create in-memory file
    output = io.StringIO()
    output.write("NHAX_FORMAT\n")
    for x, y in points:
        output.write(f"{x},{y}\n")
    return output.getvalue() 