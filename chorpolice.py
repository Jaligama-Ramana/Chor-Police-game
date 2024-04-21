#requirements
# 1 you need to run this code only in local python interpreter (pycharm, jupyter, etc) not in online environment (google colab).
# pyautogui module wont be able to take control of your keyboard in online/virtual interpreters
# 2 you need to have whatsapp application installed on your system.
# 3 no. of items in lst and lst2 should always be same
import pyautogui as py
import time
import webbrowser as wb
import random

lst=['King(10)','Queen(9)','Soilder(8)','police(7/0)','Theif(7/0)'] #add the character names along with points that you want to send to your friends as messages
#you can also play this game as Ram Sita by removing the hash of below line
# lst=['Ram(10/0)','Sita(10/0)','Hanuman(9)','lakshman(8)','Ravana(7)'] #add extra character names if there are more players
lst2=['+914857348','+91657349','+9112345','+91485340','9145245'] #enter the list of phone numbers of the players along with country code
while len(lst2)!=0:
url=f'whatsapp://send?phone={lst2.pop(random.randrange(len(lst2)))}'
wb.open_new_tab(url)
time.sleep(2)
py.write(f'you got {lst.pop(random.randrange(len(lst)))}')
py.press('enter')
py.press('enter')
