from flask import Flask, render_template, request, send_file
import os
from convert_to_nhax import extract_points_from_image, convert_points_to_nhax

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)
            points = extract_points_from_image(image_path)
            nhax_path = os.path.join(UPLOAD_FOLDER, file.filename + '.nhax')
            convert_points_to_nhax(points, nhax_path)
            return send_file(nhax_path, as_attachment=True)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_author')
def about_author():
    return render_template('about_author.html')

if __name__ == '__main__':
    app.run(debug=True) 