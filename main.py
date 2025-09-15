import yt_dlp
import shutil
import os
import re

ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg')
audio_path = 'Audio'
video_path = 'Video'
links_path = 'links.txt'

def progress_hook(d):
    if d['status'] == 'finished':
        print(f" - Download concluído: {d['filename']}")
        
opts_video = {
    'outtmpl': os.path.join(video_path, '%(title).50s.%(ext)s'),  # Nome do arquivo de saída limitado a 50 caracteres
    'restrictfilenames': True,  # Restringe os nomes dos arquivos a caracteres seguros
    'sanitize': True,  # Sanitiza o nome do arquivo para o sistema de arquivos
    'concurrent_fragments': 5,  # Ajusta o número de conexões simultâneas para vídeos HLS
    'noplaylist': False,  # Não baixa playlists, apenas vídeos individuais
    'format': 'best',  # Escolhe a melhor qualidade disponível
    'merge_output_format': None,  # Não usa ffmpeg para mesclar vídeo e áudio
    'quiet': True,  # Desativa a maioria das mensagens de saída
    'progress_hooks': [progress_hook],  # Adiciona o hook de progresso
    'ffmpeg_location': ffmpeg_path
}

opts_audio = {
    'format': 'bestaudio/best',  # Escolhe a melhor qualidade de áudio disponível
    'outtmpl': os.path.join(audio_path, '%(title).50s.%(ext)s'),  # Nome do arquivo de saída limitado a 50 caracteres
    'restrictfilenames': True,  # Restringe os nomes dos arquivos a caracteres seguros
    'postprocessors': [{  # Configurações para conversão para MP3
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # Qualidade do áudio em kbps
    }],
    'progress_hooks': [progress_hook],  # Adiciona o hook de progresso
    'quiet': True,  # Desativa a maioria das mensagens de saída
    'ffmpeg_location': ffmpeg_path
}

def ytDlpTool(ydlp_opts):
    
    # Expressão regular para encontrar URLs
    url_pattern = re.compile(r'(https?://[^\s]+)')

    # Abrir o arquivo .txt com os links, especificando a codificação 'utf-8'
    with open(links_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    for line in lines:
        links = url_pattern.findall(line)
        
        for link in links:
            try:
                with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
                    ydl.download([link])
            except yt_dlp.utils.DownloadError as e:
                print(f"Erro ao baixar conteúdo: {e}")
         
def checkPath():
    
    #Se não existir as pastas, ele cria novas
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)
        print(f" - Pasta '{audio_path}' criada para armazenar músicas.")
    if not os.path.exists(video_path):
        os.makedirs(video_path)
        print(f" - Pasta '{video_path}' criada para armazenar vídeos.")
        
    # Se não existir o arquivo, ele cria um novo. Se o arquivo existir, verifica se está vazio
    if not os.path.exists(links_path):
        with open(links_path, 'w', encoding='utf-8') as f:
            pass  # Cria o arquivo vazio
        print(f"\n - Arquivo '{links_path}' criado para inserir links. \nPor favor, adicione links para download e tente novamente.")
        return False
    else:
        with open(links_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print(f"\n - O arquivo '{links_path}' está vazio. \nPor favor, adicione links para download e tente novamente.")
            return  False
    
    return True
   
def cleanUp():
    escolha = int(input(" - Deseja limpar um(a) arquivo/pasta após o download? \n1: Não \n2: Limpar links \n3: Limpar pastas \n4: Limpar links & pastas \nOpção: "))
    if escolha == 1:
        return
    elif escolha == 2:
        with open(links_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
        return print("\n - Arquivo de Links limpo após o download!")
    elif escolha == 3:
        shutil.rmtree(audio_path)
        shutil.rmtree(video_path)
        return print("\n - Pastas de Musicas e Videos limpas após o download!")
    elif escolha == 4:
        with open(links_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
        shutil.rmtree(audio_path)
        shutil.rmtree(video_path)
        return print("\n - Arquivo de Links e pastas limpos após o download!")
    if escolha not in [1, 2, 3, 4]:
        print("Opção Inválida! Tente novamente.\n")
        cleanUp()
    
def setup():
    os.system('clear')
    status = checkPath()
    
    while status == True:
        escolha = int(input(" - Bem-vindo ao programa -\nEscolha abaixo as opções para download!\n\n1: Baixar Videos \n2: Baixar Musicas\nOpção: "))
        
        if escolha == 1:
            ytDlpTool(opts_video)
        elif escolha == 2:
            ytDlpTool(opts_audio)
        elif escolha not in [1, 2]:
            print("Opção Inválida! Tente novamente.\n")
        cleanUp()
        break
            
    print("\n - Programa finalizado.\n")
        
setup()