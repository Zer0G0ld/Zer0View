# Zer0View

Zer0View é um aplicativo moderno para visualização de imagens e vídeos no Windows, suportando uma ampla variedade de formatos.

## Funcionalidades

- **Visualização de Imagens**: Abra e visualize imagens em formatos como PNG, JPEG, BMP, e WEBP.
- **Suporte a Vídeos**: Em desenvolvimento, com suporte para formatos como MP4, AVI e MKV.
- **Interface Moderna**: Design limpo e intuitivo para uma melhor experiência do usuário.

## Pré-requisitos

Antes de executar o aplicativo, você precisará ter o seguinte instalado:

- **Python 3.x**
- **FFmpeg** (para suporte a vídeos)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Zer0G0ld/Zer0View.git
   cd Zer0View
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências a partir do `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Instale o FFmpeg seguindo as instruções do [site oficial do FFmpeg](https://ffmpeg.org/download.html).

## Uso

1. Execute o aplicativo:
   ```bash
   python main.py
   ```

2. Clique no botão "Open File" para selecionar uma imagem ou vídeo.
3. As imagens serão exibidas na interface, e a funcionalidade de vídeo está em desenvolvimento.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona uma nova feature'`).
4. Faça push para a branch (`git push origin feature/nome-da-sua-feature`).
5. Abra uma pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
