from PyQt6.QtWidgets import QApplication, QLabel, QFileDialog, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
import mimetypes
import sys

# Função para abrir imagem
def open_image(file_path, label):
    q_image = QPixmap(file_path)
    label.setPixmap(q_image)
    label.show()  # Certifique-se de mostrar o label após definir a imagem

# Função para abrir vídeo
def open_video(file_path, video_widget):
    player = QMediaPlayer()
    player.setMedia(QUrl.fromLocalFile(file_path))  # Defina diretamente a URL do arquivo
    player.setVideoOutput(video_widget)  # Define o widget de vídeo
    player.play()  # Inicia a reprodução do vídeo
    video_widget.show()  # Garante que o widget de vídeo esteja visível

# Função para processar o arquivo e decidir se é imagem ou vídeo
def process_file(label, video_widget):
    file_path, _ = QFileDialog.getOpenFileName(None, "Abrir Arquivo", "", "Imagens e Vídeos (*.png *.jpg *.jpeg *.bmp *.webp *.mp4 *.avi *.mkv)")
    if file_path:
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and mime_type.startswith('image'):
            open_image(file_path, label)
            video_widget.hide()  # Esconde o widget de vídeo se uma imagem for aberta
        elif mime_type and mime_type.startswith('video'):
            label.clear()  # Limpa o label se um vídeo for aberto
            label.hide()  # Esconde o label se um vídeo for aberto
            open_video(file_path, video_widget)

# Função principal para inicializar a interface do Zer0View
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Zer0View")
    layout = QVBoxLayout()

    # Configurações de estilo
    app.setStyleSheet("""
        QLabel {
            border: none;
            background-color: #333;
        }
        QPushButton {
            background-color: #444;
            color: #FFF;
            border-radius: 5px;
            padding: 10px;
        }
    """)

    # Label para exibir imagem
    label = QLabel()
    layout.addWidget(label)

    # Widget para exibir vídeo
    video_widget = QVideoWidget()
    layout.addWidget(video_widget)
    video_widget.hide()  # Inicialmente esconde o widget de vídeo

    # Botão para abrir o arquivo
    open_button = QPushButton("Abrir Arquivo")
    open_button.clicked.connect(lambda: process_file(label, video_widget))
    layout.addWidget(open_button)

    window.setLayout(layout)
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

# Executa o aplicativo
if __name__ == "__main__":
    main()
