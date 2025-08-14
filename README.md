````markdown
# Ferramenta Download

Ferramenta em Python para baixar vídeos ou músicas de várias plataformas utilizando:
[yt-dlp](https://github.com/yt-dlp/yt-dlp) 
[FFmpeg](https://ffmpeg.org/).  
Suporta links misturados em um arquivo `.txt`, filtrando automaticamente apenas os links válidos.

## 📋 Requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/) instalado
- [FFmpeg](https://ffmpeg.org/download.html) instalado e disponível no `PATH`
- Conexão com a internet

## 📦 Instalação

Clone o repositório e acesse a pasta:
```bash
git clone https://github.com/SEU_USUARIO/ferramenta-download-ytdlp.git
cd ferramenta-download-ytdlp
````

Instale as dependências:

```bash
poetry install
```

> 💡 Recomendo configurar o Poetry para criar o venv na pasta do projeto:
>
> ```bash
> poetry config virtualenvs.in-project true
> ```

## 📂 Estrutura do Projeto

```
ferramenta-download-ytdlp/
│
├── main.py                # Script principal para escolher vídeos ou músicas
├── Video.py               # Funções para baixar vídeos
├── Audio.py               # Funções para baixar e converter para MP3
├── links.txt              # Arquivo de texto com links para download
├── Musicas/               # Pasta de saída para músicas (criada automaticamente)
├── Videos/                # Pasta de saída para vídeos (criada automaticamente)
└── pyproject.toml         # Configuração do Poetry
```

## 📝 Como usar

1. Coloque todos os links que deseja baixar dentro do arquivo `links.txt`

   * Pode ter texto misturado com links, o script detecta automaticamente os URLs.
   * Um ou mais links por linha.

2. Execute o script:

```bash
poetry run python main.py
```

3. Escolha a opção desejada:

```
 - Bem-vindo ao programa -
Escolha abaixo as opções para download!

1: Baixar Videos
2: Baixar Musicas
Opção:
```

4. O programa baixará e salvará:

   * Vídeos na pasta `Videos/`
   * Músicas em MP3 na pasta `Musicas/`

## ⚙️ Configurações

* **Qualidade do áudio**: MP3 a 192 kbps usando FFmpeg
* **Qualidade do vídeo**: Melhor disponível (`best`)
* **Nome do arquivo**: Título limitado a 50 caracteres, sem caracteres inválidos
* **Links**: Pode baixar vídeos de YouTube, TikTok, Instagram, Twitter, entre outros suportados pelo yt-dlp

## 🚫 Erros comuns

* **`ffmpeg not found`** → Instale o FFmpeg e adicione ao PATH
* **`'utf-8' codec can't decode byte`** → Certifique-se de salvar `links.txt` com codificação UTF-8
* **`DownloadError`** → Link inválido, indisponível ou protegido

## 📜 Licença

Uso pessoal. Respeite os termos de serviço das plataformas de onde os conteúdos são baixados.
