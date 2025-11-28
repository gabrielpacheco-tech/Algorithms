#This script automatically Qeues in a League of Legends ranked solo/duo match in the lane you've chosen (it is in Portuguese and those files are on my PC)

import pyautogui
import time

pyautogui.PAUSE = 1.5

caminho_imagem_jogar = r"C:\Users\gabri\OneDrive\Imagens\lolzin.png"
caminho_imagem_rank_soloduo = r"C:\Users\gabri\OneDrive\Imagens\rank_soloduo.png"
caminho_imagem_confirmar = r"C:\Users\gabri\OneDrive\Imagens\confirmar.png"
caminho_imagem_encontrar_partida = r"C:\Users\gabri\OneDrive\Imagens\encontrar_partida.png"
caminho_imagem_clicar_no_lolzin = r"C:\Users\gabri\OneDrive\Imagens\clicar_no_lolzin.png"
caminho_imagem__aceitar = r"C:\Users\gabri\OneDrive\Imagens\aceitar.png"    
caminho_imagem__summoners_rift = r"C:\Users\gabri\OneDrive\Imagens\summoners_rift.png"
caminho_imagem__adc = r"C:\Users\gabri\OneDrive\Imagens\adc.png" 
caminho_imagem__suporte = r"C:\Users\gabri\OneDrive\Imagens\suporte.png"
caminho_imagem__mid = r"C:\Users\gabri\OneDrive\Imagens\mid.png"
caminho_imagem__jungle = r"C:\Users\gabri\OneDrive\Imagens\jungle.png"
caminho_imagem__top = r"C:\Users\gabri\OneDrive\Imagens\top.png"
caminho_imagem__preencher = r"C:\Users\gabri\OneDrive\Imagens\preencher.png"

def localizar_seguro(caminho, confidence=0.9, grayscale=False):
    try:
        return pyautogui.locateOnScreen(caminho, confidence=confidence, grayscale=grayscale)
    except pyautogui.ImageNotFoundException:
        return None

def localizar_center_seguro(caminho, confidence=0.9, grayscale=False):
    try:
        return pyautogui.locateCenterOnScreen(caminho, confidence=confidence, grayscale=grayscale)
    except pyautogui.ImageNotFoundException:
        return None

def clicar_se_existe(localizacao):
    if localizacao:
        pyautogui.click(localizacao)
        return True
    return False

def ler_lane():
    try:
        return int(input("Digite a sua lane: "))
    except:
        return 0 

print("\n\nQual lane vai jogar??")
print("\n 1- ADC \n 2 - Suporte \n 3 - Jungle \n 4 - Top \n 5 - Mid \n 6 - Preencher \n")

lane = ler_lane()

while not (lane >= 1 and lane <= 6):
    print("Por favor, digite um número inteiro de 1 a 6!\n")
    lane = ler_lane()

while True:
    if lane >=1 and lane <=6:          
        print("\n")
        pyautogui.press("win")
        pyautogui.write("League")
        pyautogui.press("enter")
        pyautogui.hotkey('win', 'tab', interval=0.1)

        while True:
            try:
                localizacao_lolzin = pyautogui.locateOnScreen(caminho_imagem_clicar_no_lolzin, confidence=0.8, grayscale=True)
                if localizacao_lolzin:  
                    print("LOL encontrado! \n")
                    imagem_lolzin = pyautogui.locateCenterOnScreen(caminho_imagem_clicar_no_lolzin, confidence=0.8, grayscale=True)                
                    pyautogui.click(imagem_lolzin)

                while True:    
                    try:
                        localizacao_jogar = pyautogui.locateOnScreen(caminho_imagem_jogar, confidence=0.9, grayscale=True)        
                        if localizacao_jogar:
                            print("Jogar encontrado! \n")
                            imagem_jogar = pyautogui.locateCenterOnScreen(caminho_imagem_jogar, confidence=0.8, grayscale=True)                
                            pyautogui.click(imagem_jogar)
                            imagem_summoners_rift = pyautogui.locateCenterOnScreen(caminho_imagem__summoners_rift, confidence=0.8, grayscale=True)
                            pyautogui.click(imagem_summoners_rift)
                            imagem_rank = pyautogui.locateCenterOnScreen(caminho_imagem_rank_soloduo, confidence=0.8, grayscale=True)
                            pyautogui.click(imagem_rank)

                            imagem_confirmar = localizar_center_seguro(caminho_imagem_confirmar, confidence=0.8, grayscale=True)
                            clicar_se_existe(imagem_confirmar)
                            time.sleep(2)
                            localizacao_adc = localizar_seguro(caminho_imagem__adc, confidence=0.9)
                            localizacao_suporte = localizar_seguro(caminho_imagem__suporte, confidence=0.9)
                            localizacao_jungle = localizar_seguro(caminho_imagem__jungle, confidence=0.9)
                            localizacao_top = localizar_seguro(caminho_imagem__top, confidence=0.9)
                            localizacao_mid = localizar_seguro(caminho_imagem__mid, confidence=0.9)
                            localizacao_preencher = localizar_seguro(caminho_imagem__preencher, confidence=0.9)
                            lane_select = (
                                localizacao_adc or localizacao_suporte or localizacao_jungle or
                                localizacao_mid or localizacao_top or localizacao_preencher
                            )
                            imagem_encontrar_partida = localizar_center_seguro(caminho_imagem_encontrar_partida, confidence=0.85, grayscale=True)

                            if lane == 1: #ADC
                                print("Lane escolhida: ADC \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane ADC... \n")
                                    clicar_se_existe(localizacao_adc)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'...")
                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2)     

                            if lane == 2: #SUPORTE
                                print("Lane escolhida: SUPORTE \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane SUPORTE... \n")
                                    clicar_se_existe(localizacao_suporte)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'... \n")

                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2)                        

                            if lane == 3: #JUNGLE
                                print("Lane escolhida: JUNGLE \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane JUNGLE... \n")
                                    clicar_se_existe(localizacao_jungle)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'... \n")

                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2)

                            if lane == 4: #TOP
                                print("Lane escolhida: TOP \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane TOP... \n")
                                    clicar_se_existe(localizacao_top)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'... \n")

                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2)

                            if lane == 5: #MID
                                print("Lane escolhida: MID \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane MID... \n")
                                    clicar_se_existe(localizacao_mid)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'... \n")

                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2) 
                            
                            if lane == 6: #PREENCHER
                                print("Lane escolhida: PREENCHER \n")
                                if lane_select:
                                    print("Lane atual encontrada, clicando nela... \n")
                                    clicar_se_existe(lane_select)
                                    time.sleep(2)
                                    print("Clicando no ícone da lane PREENCHER... \n")
                                    clicar_se_existe(localizacao_preencher)
                                else:
                                    print("Nenhuma lane encontrada na tela! \n")
                                clicar_se_existe(imagem_encontrar_partida)
                                print("Aguardando 'Aceitar'... \n")

                                while True:
                                    localizacao_aceitar = localizar_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    imagem_aceitar = localizar_center_seguro(caminho_imagem__aceitar, confidence=0.8, grayscale=True)
                                    if localizacao_aceitar:
                                        print("Partida encontrada! Aceitando! \n")
                                        pyautogui.click(imagem_aceitar)
                                        break
                                    print("Tentando localizar 'Aceitar'... \n")
                                    time.sleep(2) 

                    except pyautogui.ImageNotFoundException:
                        print("Tentando localizar 'JOGAR'... \n")
                        time.sleep(3)      
            except pyautogui.ImageNotFoundException:
                print("Tentando localizar 'O LOL'... \n")
                time.sleep(3)                      

