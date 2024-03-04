from pywinauto import  keyboard, mouse
from keyboard import  wait
from threading import Thread
import pygetwindow as gw
import time

# variável booleana que será usada na thread
is_pressed = False


def update_steps():
    # deixo a variável global para que a thread possa alterar o valor
    global is_pressed

    # pega a janela do jogo
    wins = gw.getWindowsWithTitle('Skyrim Special Edition')
    print(wins)
    win = wins[0]
    # ativa a janela do jogo
    win.activate()
    # espera 4 segundos, para dar tempo do jogo ser ativado
    time.sleep(4)    
    # aperta a tecla 'ESC' para fechar o menu de Skyrim
    keyboard.send_keys('{ESC}')
    
    while not is_pressed:
        time.sleep(0.5)
        
        # Aperto o botão esquerdo e direito do mouse 3 vezes
        for i in range(3):
            mouse.press(button='left', coords=(0, 0))
            mouse.press(button='right', coords=(0, 0))
     
            time.sleep(1)
            mouse.release(button='left', coords=(0, 0))
            mouse.release(button='right', coords=(0, 0))
        
        time.sleep(0.5)
        # aperto T para abrir o menu de tempo
        keyboard.send_keys('{t down}')
        keyboard.send_keys('{t up}')
        time.sleep(0.5)
        # aperto ENTER para esperar 1 hora no jogo
        keyboard.send_keys('{ENTER}')

# função que será executada na thread
def event_listener():
    global is_pressed
    # espero X ser pressionada para alterar a variável
    wait('x')
    is_pressed = True
    return


def main():
    # crio a thread e passo como target a função para alterar a variável
    t = Thread(target=event_listener)
    t.start()
    update_steps()
    t.join()


if __name__ == '__main__':
    main()     