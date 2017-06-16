def cronometro(segundos):
    import pygame

    secs = 0
    x = segundos
    contador = 0
    while secs < x:
        clock = pygame.time.Clock()
        contador += 1
        if contador == 60:
            secs += 1
            contador = 0
        time_passed = clock.tick(60)
    return secs



