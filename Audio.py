import yt_dlp
import os
import re

# Função para exibir uma mensagem quando o download é concluído
def progress_hook(d):
    if d['status'] == 'finished':
        print(f" - Download concluído: {d['filename']}")

# Função para baixar vídeos e converter para MP3
def baixar_audio_mp3(file_path, pasta_destino):
    # Garantir que a pasta de destino exista, e se não, criá-la
    os.makedirs(pasta_destino, exist_ok=True)

    # Expressão regular para encontrar URLs
    url_pattern = re.compile(r'(https?://[^\s]+)')

    # Abrir o arquivo .txt com os links, especificando a codificação 'utf-8'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Iterar sobre cada linha do arquivo
    for line in lines:
        # Buscar todas as URLs válidas na linha
        links = url_pattern.findall(line)

        # Baixar e converter cada URL encontrada para MP3
        for link in links:
            # Configurações da API yt-dlp para converter para MP3
            ydl_opts = {
                'format': 'bestaudio/best',  # Escolhe a melhor qualidade de áudio disponível
                'outtmpl': os.path.join(pasta_destino, '%(title).50s.%(ext)s'),  # Nome do arquivo de saída limitado a 50 caracteres
                'restrictfilenames': True,  # Restringe os nomes dos arquivos a caracteres seguros
                'postprocessors': [{  # Configurações para conversão para MP3
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',  # Qualidade do áudio em kbps
                }],
                'progress_hooks': [progress_hook],  # Adiciona o hook de progresso
                'quiet': True,  # Desativa a maioria das mensagens de saída
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
            except yt_dlp.utils.DownloadError as e:
                print(f"Erro ao baixar o vídeo: {e}")

