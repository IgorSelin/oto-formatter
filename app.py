from flask import Flask, render_template, request, send_file, send_from_directory
import os
from convert_to_nhax import extract_points_from_image, convert_points_to_nhax
import io

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_author')
def about_author():
    return render_template('about_author.html')

@app.route('/download-example')
def download_example():
    return send_file('examples/Горохов Дмитро.nhax', as_attachment=True)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    if file:
        # Read the image file
        image_data = file.read()
        
        # Convert to NHAX
        nhax_data = convert_points_to_nhax(extract_points_from_image(image_data))
        
        # Generate filename
        filename = os.path.splitext(file.filename)[0] + '.nhax'
        
        # Return the NHAX file
        return send_file(
            io.BytesIO(nhax_data),
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name=filename
        )

if __name__ == '__main__':
    app.run(debug=True) 