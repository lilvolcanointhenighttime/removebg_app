from flask import Flask, render_template, request, send_file
from rembg import remove
import io

app = Flask(__name__, static_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    file = request.files['file'].read()
    result = remove(file)
    result_image = io.BytesIO(result)
    result_image.seek(0)
    return send_file(result_image, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
