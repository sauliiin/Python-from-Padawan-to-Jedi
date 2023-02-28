import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


'O pygame.init é um comando necessário para iniciar o paygame. Segundo o prof, a gente não precisa conhecer todos os módulos'
'sem paranóia de conhecer todos. O ideal é conhecer uma quantidade boa que seja um bom canivete suiço'

'como adicionar música? copia a musica onde ela está e clica em cima de uma das aulas e paste'

'dica da galera: No lugar de colocar o input vc pode iniciar o mixer antes do pygame, assim o programa não fica aguardando o input do usuario'
#import pygame
#pygame.mixer.init()
#pygame.init()
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

#fica esperto e googla os modulos: https://www.pygame.org/docs/ref/mixer.html

