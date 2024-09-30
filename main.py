from video import progress_hook, baixar_videos
from audio import progress_hook, baixar_audio_mp3

# Caminho do arquivo .txt com os links dos videos/musicas
caminho_txt = 'links.txt'

# Caminho da pasta onde os arquivos MP3 serão salvos
pasta_audio = 'Musicas'

# Caminho da pasta onde os vídeos serão salvos
pasta_video = 'Videos'

escolha = int(input(" - Bem-vindo ao programa -\nEscolha abaixo as opções para download!\n\n1: Baixar Videos \n2: Baixar Musicas\nOpção: "))

if escolha == 1:
    baixar_videos(caminho_txt, pasta_video)
if escolha == 2:
    baixar_audio_mp3(caminho_txt, pasta_audio)