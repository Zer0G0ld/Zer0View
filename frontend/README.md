# Frontend - Zer0View

Este é o frontend do projeto Zer0View, que utiliza **React**, **Vite**, **Styled-Components** e **TypeScript** para criar uma interface moderna e interativa para visualização de imagens e vídeos.

## Passos para Configuração e Desenvolvimento

### 1. Instalar as Dependências

Primeiro, você precisa instalar as dependências do projeto. Execute os seguintes comandos para instalar as dependências principais e de desenvolvimento:

```bash
npm install react react-dom styled-components
npm install --save-dev typescript @types/react @types/react-dom
npm install
```

Esse comando vai instalar todas as dependências necessárias para o funcionamento do frontend.

### 2. Estrutura Inicial

Após instalar as dependências, vamos modificar a estrutura do projeto. Dentro da pasta `src/`, execute os seguintes passos:

- **Apague** todo o conteúdo dentro de `src/`, exceto o arquivo `main.tsx`.
- Crie as seguintes pastas e arquivos dentro de `src/`:

#### a) **Pasta `components/`**

Crie dois arquivos de componentes:

- `Button.tsx` – Componente de botão reutilizável.
- `Gallery.tsx` – Componente para exibir a galeria de imagens.

#### b) **Pasta `styles/`**

Crie dois arquivos para gerenciar os estilos globais e o tema:

- `GlobalStyles.ts` – Arquivo para definir os estilos globais da aplicação.
- `theme.ts` – Arquivo para configurar o tema da aplicação (cores, fontes, etc.).

#### c) **Arquivo `api.ts`**

Crie o arquivo `api.ts` onde você organizará as requisições para o backend, como o upload de imagens e a recuperação das imagens na galeria.

### 3. Atualizar `package.json`

Agora, vamos configurar os scripts no arquivo `package.json` para facilitar o desenvolvimento simultâneo do frontend e do backend.

Abra o arquivo `package.json` e altere a seção de `scripts` para o seguinte:

```json
"scripts": {
  "dev": "concurrently \"npm run dev:frontend\" \"npm run dev:backend\"",
  "dev:frontend": "vite",
  "dev:backend": "cd ../backend && python3 app.py",
  "build": "tsc -b && vite build",
  "lint": "eslint .",
  "preview": "vite preview"
},
```

Esses scripts fazem o seguinte:
- `dev`: Inicia tanto o frontend quanto o backend ao mesmo tempo usando o pacote `concurrently`.
- `dev:frontend`: Inicia o Vite para o desenvolvimento do frontend.
- `dev:backend`: Inicia o servidor Flask do backend.
- `build`: Compila o código TypeScript e cria a build do frontend.
- `lint`: Verifica o código com o ESLint para garantir a qualidade do código.
- `preview`: Exibe a versão de produção da aplicação localmente.

### 4. Instalar `concurrently`

Para rodar o frontend e o backend ao mesmo tempo, você precisará instalar o pacote `concurrently`. Execute o seguinte comando para instalá-lo:

```bash
npm install concurrently --save-dev
```

Este pacote permite que você execute múltiplos comandos simultaneamente. Com isso, você poderá iniciar o frontend e o backend ao mesmo tempo com o comando:

```bash
npm run dev
```

### 5. Iniciar o Frontend e o Backend

Agora, você pode iniciar o desenvolvimento tanto do frontend quanto do backend com o comando:

```bash
npm run dev
```

Isso vai iniciar o frontend (Vite) e o backend (Flask) simultaneamente. O frontend estará disponível em `http://localhost:5173/`, enquanto o backend estará em `http://localhost:5000/`.

### 6. Construção e Pré-visualização

Para construir o frontend para produção, use o seguinte comando:

```bash
npm run build
```

E para pré-visualizar a build, execute:

```bash
npm run preview
```

### 7. Linting

Se você precisar rodar o **eslint** para verificar o código por erros de formatação ou problemas de estilo, use o comando:

```bash
npm run lint
```
