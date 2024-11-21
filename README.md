# Zer0View

Zer0View é um aplicativo moderno para visualização de imagens e vídeos no Windows, suportando uma ampla variedade de formatos. Ele é composto por um backend em Flask para gerenciamento de uploads de mídia e um frontend em React com Vite e Styled-Components para uma interface moderna.

## Estrutura do Projeto

```bash
ZeroView/
├── backend/               # Backend com Python (Flask)
│   ├── static/            # Arquivos estáticos (imagens, CSS, etc.)
│   ├── uploads/           # Imagens e vídeos carregados
│   ├── app.py             # Código principal da API
│   ├── requirements.txt   # Dependências do Python
│   └── ...                # Outros arquivos/backend específicos
│
├── frontend/              # Frontend com React e Vite
│   ├── public/            # Arquivos públicos acessíveis diretamente
│   │   └── index.html     # Arquivo HTML principal
│   ├── src/               # Código-fonte React
│   │   ├── components/    # Componentes reutilizáveis
│   │   │   └── Gallery.tsx # Componente da galeria
│   │   ├── styles/        # Estilos com Styled-Components
│   │   ├── App.tsx        # Componente principal
│   │   └── main.tsx       # Arquivo de entrada do React (usando Vite)
│   ├── package.json       # Configuração do Node.js (dependências do frontend)
│   └── vite.config.ts     # Configuração do Vite para o React
│
├── README.md              # Documentação do projeto
├── .gitignore             # Arquivos e pastas ignorados pelo Git
└── ...                    # Outros arquivos de configuração
```

## Funcionalidades

- **Visualização de Imagens**: Abra e visualize imagens em formatos como PNG, JPEG, BMP, e WEBP.
- **Suporte a Vídeos**: Em desenvolvimento, com suporte para formatos como MP4, AVI e MKV.
- **Upload de Imagens**: Permite o upload de imagens para o servidor, armazenando-as na pasta `static/uploads`.
- **Interface Moderna**: Design limpo e intuitivo, com uso de **Styled-Components** para a estilização no frontend.

## Tecnologias

- **Backend**: Flask, para gerenciamento de uploads e APIs RESTful.
- **Frontend**: React com **Vite** como bundler e **Styled-Components** para a estilização.
- **Armazenamento de Mídia**: Imagens são armazenadas na pasta `static/uploads` do backend.
- **Upload de Arquivos**: Suporta upload de imagens e vídeos com extensões específicas.

## Pré-requisitos

Antes de executar o aplicativo, você precisará ter o seguinte instalado:

- **Python 3.x**
- **FFmpeg** (para suporte a vídeos no futuro)
- **Node.js** (para o frontend)
- **Yarn ou npm** (para gerenciamento de pacotes do frontend)

## Instalação

### Backend

1. Clone o repositório:
   ```bash
   git clone https://github.com/Zer0G0ld/Zer0View.git
   cd Zer0View/backend
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

5. Instale o **FFmpeg** seguindo as instruções do [site oficial do FFmpeg](https://ffmpeg.org/download.html).

### Frontend

1. Navegue até o diretório do frontend:
   ```bash
   cd Zer0View/frontend
   ```

2. Instale as dependências com **npm** ou **yarn**:
   ```bash
   npm install
   ```

   ou

   ```bash
   yarn install
   ```

3. Execute o frontend com o comando:
   ```bash
   npm run dev
   ```

   O aplicativo frontend estará disponível em `http://localhost:5173/`.

### Rodando o Backend

1. Navegue até o diretório do backend:
   ```bash
   cd Zer0View/backend
   ```

2. Execute o backend:
   ```bash
   python app.py
   ```

   O backend estará disponível em `http://localhost:5000/`.

## Como Usar

1. Acesse o frontend através do navegador em `http://localhost:5173/`.
2. O usuário pode **enviar imagens** usando a interface de upload, que será salva no servidor.
3. As imagens carregadas serão exibidas na galeria, que é alimentada pela API do backend.

   - **Função de upload**: O frontend envia uma requisição `POST` para a rota `/api/upload` do backend.
   - **Visualização**: As imagens são recuperadas pela rota `GET /api/images` do backend e exibidas dinamicamente na galeria.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona uma nova feature'`).
4. Faça push para a branch (`git push origin feature/nome-da-sua-feature`).
5. Abra uma pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

