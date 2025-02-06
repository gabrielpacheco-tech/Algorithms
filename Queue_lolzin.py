import pyautogui
import time

caminho_imagem_jogar = r"C:\Users\gabri\OneDrive\Imagens\lolzin.png"
caminho_imagem_rank_soloduo = r"C:\Users\gabri\OneDrive\Imagens\rank_soloduo.png"
caminho_imagem_confirmar = r"C:\Users\gabri\OneDrive\Imagens\confirmar.png"
caminho_imagem_encontrar_partida = r"C:\Users\gabri\OneDrive\Imagens\encontrar_partida.png"
caminho_imagem_clicar_no_lolzin = r"C:\Users\gabri\OneDrive\Imagens\clicar_no_lolzin.png"
caminho_imagem__aceitar = r"C:\Users\gabri\OneDrive\Imagens\aceitar.png"    

pyautogui.PAUSE = 2.0

print("Qual lane vai jogar??")
print("\n 1- ADC \n 2 - Suporte \n 3 - Jungle \n 4 - Top \n 5 - Mid \n")
lane = int(input("Digite a sua lane: " ))
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
                localizacao_jogar = pyautogui.locateOnScreen(caminho_imagem_jogar, confidence=0.8, grayscale=True)

                if localizacao_jogar:
                    print("Jogar encontrado! \n")
                    imagem_jogar = pyautogui.locateCenterOnScreen(caminho_imagem_jogar, confidence=0.8, grayscale=True)                
                    pyautogui.click(imagem_jogar)
                    imagem_rank = pyautogui.locateCenterOnScreen(caminho_imagem_rank_soloduo, confidence=0.8, grayscale=True)
                    pyautogui.click(imagem_rank)
                    imagem_confirmar = pyautogui.locateCenterOnScreen(caminho_imagem_confirmar, confidence=0.8, grayscale=True)
                    pyautogui.click(imagem_confirmar)
                    time.sleep(3)
                    imagem_encontrar_partida = pyautogui.locateCenterOnScreen(caminho_imagem_encontrar_partida, confidence=0.6, grayscale=True)
                    imagem_aceitar = pyautogui.locateCenterOnScreen(caminho_imagem_encontrar_partida, confidence=0.8, grayscale=True)

                    if lane == 1: #ADC
                        pyautogui.click(x=691, y=617)
                        pyautogui.click(x=707, y=572)
                        pyautogui.click(x=723, y=616)
                        pyautogui.click(x=695, y=571)
                        pyautogui.click(imagem_encontrar_partida)                     
                    if lane == 2: #SUPORTE
                        pyautogui.click(x=691, y=617)
                        pyautogui.click(x=751, y=570)
                        pyautogui.click(x=723, y=616)
                        pyautogui.click(x=695, y=571)
                        pyautogui.click(imagem_encontrar_partida) 
                    if lane == 3: #JUNGLE
                        pyautogui.click(x=691, y=617)
                        pyautogui.click(x=621, y=572)
                        pyautogui.click(x=723, y=616)
                        pyautogui.click(x=695, y=571)
                        pyautogui.click(imagem_encontrar_partida)
                    if lane == 4: #TOP
                        pyautogui.click(x=691, y=617)
                        pyautogui.click(x=577, y=569)
                        pyautogui.click(x=723, y=616)
                        pyautogui.click(x=695, y=571)
                        pyautogui.click(imagem_encontrar_partida)                        
                    if lane == 5: #MID      
                        pyautogui.click(x=691, y=617)
                        pyautogui.click(x=664, y=572)
                        pyautogui.click(x=723, y=616)
                        pyautogui.click(x=577, y=569)
                        pyautogui.click(imagem_encontrar_partida) 
                    break

            except pyautogui.ImageNotFoundException:
                print("Tentando localizar 'JOGAR'...")
                time.sleep(3)      
    except pyautogui.ImageNotFoundException:
            print("Tentando localizar 'O LOL'...")
            time.sleep(3)      