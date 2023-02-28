import time
import emoji

for cont in range(10, -1, -1):
    print(cont)
    time.sleep(0.5)
print('Boooommmm!')
time.sleep(2.5)
print(emoji.emojize(':fireworks:'*5))