from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image provided', 400

    file = request.files['image']
    input_image = file.read()
    output_image = remove(input_image)

    return send_file(
        io.BytesIO(output_image),
        mimetype='image/png',
        as_attachment=True,
        download_name='no-bg.png'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)