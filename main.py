from Video import progress_hook, baixar_videos
from Audio import progress_hook, baixar_audio_mp3

def limpeza_txt():
    with open(caminho_txt, 'w', encoding='utf-8') as f:
        f.truncate(0)
    return print(" - Arquivo de Links limpo após o download!")

caminho_txt = 'links.txt'
pasta_audio = 'Musicas'
pasta_video = 'Videos'

escolha = int(input(" - Bem-vindo ao programa -\nEscolha abaixo as opções para download!\n\n1: Baixar Videos \n2: Baixar Musicas\nOpção: "))

if escolha == 1:
    baixar_videos(caminho_txt, pasta_video)
    limpeza_txt()
if escolha == 2:
    baixar_audio_mp3(caminho_txt, pasta_audio)
    limpeza_txt()
if escolha not in [1, 2]:
    print("Opção Inválida!")

