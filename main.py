import pyautogui
import time
import pandas 

pyautogui.PAUSE = 1
# entrar no site

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.click(x=800, y=600, button='left') # move, then click the left mouse button.
link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")
time.sleep(3)


# fazer login
pyautogui.click(x=595, y=460)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")
pyautogui.click(x=944, y=668)
time.sleep(5)

# importar base de dados
tabela  = pandas.read_csv("produtos.csv")

# cadastrar produto para toda base de dados
for linha in tabela.index:
    pyautogui.click(x=600, y=326)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
            
    # envio produto
    pyautogui.click(x=840, y=697)
    pyautogui.scroll(1000)