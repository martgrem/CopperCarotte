





def jeu(fenetre) :
    cont = True

    #fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pos_fenetre = fenetre.get_rect()
    fond = pygame.image.load("CopperCarotte/dossier top secret/menu/fond d'écran menu.jpg").convert()
    fond = pygame.transform.scale(fond, pos_fenetre.size)

    boum = pygame.image.load("neauteubouqueux/PyGame/BOUM.png").convert_alpha()
    boum = pygame.transform.scale(boum, (800, 800))
    fenetre.blit(fond, (0, 0))
    fenetre.blit(boum, (300, 100))
    pygame.display.flip()
    while cont:    
        

        


        for event in pygame.event.get():
            if event.type == QUIT:
                cont=False
                pygame.display.quit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    cont=False
                    pygame.display.quit()










