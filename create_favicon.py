from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon(size, output_path):
    # Create a new image with a transparent background
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Calculate font size (approximately 70% of the image size)
    font_size = int(size * 0.7)
    
    # Try to use a system font, fall back to default if not available
    try:
        font = ImageFont.truetype("Arial", font_size)
    except:
        font = ImageFont.load_default()
    
    # Draw the letter "N"
    text = "N"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate position to center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw the text with a gradient effect
    for i in range(3):
        draw.text((x-i, y), text, font=font, fill=(59, 139, 235, 255))  # #3b8beb
        draw.text((x+i, y), text, font=font, fill=(108, 160, 220, 255))  # #6ca0dc
    
    # Save the image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)

def main():
    # Create favicon directory if it doesn't exist
    favicon_dir = "static/favicon"
    os.makedirs(favicon_dir, exist_ok=True)
    
    # Generate different sizes
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512
    }
    
    for filename, size in sizes.items():
        output_path = os.path.join(favicon_dir, filename)
        create_favicon(size, output_path)
        print(f"Created {filename}")

if __name__ == "__main__":
    main() 