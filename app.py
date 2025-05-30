from flask import Flask, render_template, request, send_file
import os
from convert_to_nhax import extract_points_from_image, convert_points_to_nhax
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read file data into memory
            file_data = file.read()
            # Process the image
            points = extract_points_from_image(file_data)
            # Convert to NHAX format
            nhax_data = convert_points_to_nhax(points)
            # Create in-memory file
            nhax_file = io.BytesIO(nhax_data.encode())
            nhax_file.seek(0)
            # Send the file
            return send_file(
                nhax_file,
                mimetype='text/plain',
                as_attachment=True,
                download_name=f"{file.filename}.nhax"
            )
    return render_template('index.html')

@app.route('/download-example')
def download_example():
    example_path = os.path.join('examples', 'Горохов Дмитро.nhax')
    return send_file(
        example_path,
        mimetype='text/plain',
        as_attachment=True,
        download_name='example.nhax'
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_author')
def about_author():
    return render_template('about_author.html')

if __name__ == '__main__':
    app.run(debug=True) 