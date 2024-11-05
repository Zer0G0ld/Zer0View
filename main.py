from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSlider
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl, QPropertyAnimation, QEasingCurve, Qt
import mimetypes
import sys

class Zer0View(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zer0View")
        self.resize(900, 600)
        
        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Configuração de estilo
        self.setStyleSheet("""
        QWidget {
            background-color: #222;
            color: #FFF;
        }
        QLabel {
            border: 1px solid #444;
            border-radius: 10px;
            padding: 20px;
        }
        QPushButton {
            background-color: #444;
            color: #FFF;
            border-radius: 5px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #555;  /* Cor quando o mouse passa sobre o botão */
        }
        QSlider {
            margin: 10px;
            background: #444;
        }
        """)
        
        # Label para exibir imagens
        self.label = QLabel()
        self.label.setScaledContents(True)  # Permite redimensionar a imagem
        self.layout.addWidget(self.label)

        # Slider para controlar a exibição de imagens
        self.image_slider = QSlider(Qt.Orientation.Horizontal)
        self.image_slider.setRange(0, 0)  # Inicialmente, o range é 0
        self.image_slider.valueChanged.connect(self.update_image)
        self.layout.addWidget(self.image_slider)

        # Widget de vídeo e player
        self.video_widget = QVideoWidget()
        self.layout.addWidget(self.video_widget)
        self.video_widget.hide()  # Esconde o widget de vídeo inicialmente
        
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self.video_widget)
        
        # Botão para abrir arquivo
        self.open_button = QPushButton("Abrir Arquivo")
        self.open_button.clicked.connect(self.process_file)
        self.layout.addWidget(self.open_button)

        # Botão para reproduzir/pausar vídeo
        self.play_button = QPushButton("Reproduzir/Pausar Vídeo")
        self.play_button.clicked.connect(self.toggle_play_pause)
        self.layout.addWidget(self.play_button)

        # Animação do botão
        self.animation = QPropertyAnimation(self.open_button, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)

        # Lista de imagens e índice atual
        self.image_files = []
        self.current_image_index = 0

    # Função para abrir imagem
    def open_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.label.setPixmap(pixmap)
        self.label.setFixedSize(self.size())  # Ajusta o tamanho do QLabel
        self.label.show()
        self.video_widget.hide()  # Esconde o widget de vídeo se uma imagem for aberta

    # Função para abrir vídeo
    def open_video(self, file_path):
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.player.play()
        self.video_widget.setFixedSize(self.size())  # Ajusta o tamanho do QVideoWidget
        self.video_widget.show()  # Mostra o widget de vídeo
        self.label.hide()  # Esconde o label de imagem se um vídeo for aberto
    
    # Função para processar o arquivo e decidir se é imagem ou vídeo
    def process_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Imagens e Vídeos (*.png *.jpg *.jpeg *.bmp *.webp *.mp4 *.avi *.mkv *.webm)")
        if file_path:
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type and mime_type.startswith('image'):
                self.open_image(file_path)
                self.image_files.append(file_path)
                self.image_slider.setRange(0, len(self.image_files) - 1)  # Atualiza o range do slider
            elif mime_type and mime_type.startswith('video'):
                self.open_video(file_path)
                self.image_slider.setRange(0, 0)  # Reseta o range do slider para 0 se um vídeo for aberto

        # Executa a animação
        self.animate_button()

    def update_image(self):
        if self.image_files:
            self.current_image_index = self.image_slider.value()
            self.open_image(self.image_files[self.current_image_index])

    def toggle_play_pause(self):
        if self.player.state() == QMediaPlayer.State.Playing:
            self.player.pause()
        else:
            self.player.play()

    def animate_button(self):
        self.animation.setStartValue(self.open_button.geometry())
        self.animation.setEndValue(self.open_button.geometry().adjusted(0, 0, 0, 10))  # Aumenta a altura do botão
        self.animation.start()

# Função principal para inicializar a interface do Zer0View
def main():
    app = QApplication(sys.argv)
    window = Zer0View()
    window.show()
    sys.exit(app.exec())

# Executa o aplicativo
if __name__ == "__main__":
    main()
