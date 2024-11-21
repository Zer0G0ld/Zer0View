from flask import Flask, jsonify, request, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Diretório para armazenar as imagens
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tipos de arquivo permitidos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'mp4', 'ico', 'svg'}

# Função para verificar as extensões permitidas
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/images', methods=['GET'])
def get_images():
    # Lista de imagens armazenadas na pasta 'static/uploads'
    images = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if allowed_file(filename):
            images.append({"id": len(images) + 1, "url": f"/static/uploads/{filename}"})
    return jsonify(images)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Verifica se a chave 'image' está presente no pedido
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['image']
    
    # Verifica se o arquivo possui um nome
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Verifica se o arquivo já existe, para evitar sobreescrever
        if os.path.exists(file_path):
            return jsonify({'message': 'File already exists'}), 409
        
        # Salva o arquivo na pasta 'static/uploads'
        file.save(file_path)
        return jsonify({'message': 'File successfully uploaded', 'url': f'/static/uploads/{filename}'}), 200
    else:
        return jsonify({'message': 'File type not allowed. Allowed types are: png, jpg, jpeg, gif, bmp, webp, mp4, ico, svg'}), 400

@app.route('/static/uploads/<path:filename>')
def serve_uploaded_file(filename):
    # Serve arquivos da pasta 'static/uploads'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'message': 'File not found'}), 404
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    # Cria o diretório de uploads, caso não exista
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)
