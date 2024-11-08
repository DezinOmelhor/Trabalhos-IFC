#https://sig.ifc.edu.br/sigaa/expirada.jsp (2 ENTER)
import pyautogui
import keyboard
import time

# Abrir o Navegador
pyautogui.press('win')  # Open Start menu

time.sleep(3)

pyautogui.write('firefox') # Type the application name

time.sleep(3)

pyautogui.press('enter')  # Open the application

# Esperar o navegador abrir e pesquisar pelo site
time.sleep(7)

pyautogui.write ('sig.ifc.edu.br')
pyautogui.press ('Enter')

time.sleep(7)

# pyautogui.press ('Enter')
pyautogui.write ('Seu Nome de Usuário') #Escreva seu nome de usuário
pyautogui.press ('tab') #Pular um
pyautogui.write ('Sua Senha') #Escreva sua senha
pyautogui.press ('Enter')

time.sleep(7)

for i in range (25):
    pyautogui.press ('tab')

pyautogui.press ('Enter')

time.sleep(3)