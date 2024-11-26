import pygame

# Initialisation
pygame.init()
fen = pygame.display.set_mode((800, 600))
couleur_rond = (0, 255, 255)
couleur_fond = (0, 0, 0)
couleur_texte = (100, 50, 200)

# Coordonnées initiales du rond
x = 400
y = 300
vitesse = 200  # Vitesse du cercle en pixels par seconde

police = pygame.font.Font(None, 36)

# Création d'une horloge pour gérer le delta time
clock = pygame.time.Clock()

# Boucle principale
continuer = True
while continuer:
    # Calcul du delta time
    dt = clock.tick(60) / 1000  # Convertir en secondes

    # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    # Récupération de l'état des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_z]:  # Haut
        y -= vitesse * dt
    if touches[pygame.K_s]:  # Bas
        y += vitesse * dt
    if touches[pygame.K_q]:  # Gauche
        x -= vitesse * dt
    if touches[pygame.K_d]:  # Droite
        x += vitesse * dt

    # Mise à jour de l'affichage
    fen.fill(couleur_fond)
    pygame.draw.circle(fen, couleur_rond, (int(x), int(y)), 40)

      # Calcul et affichage des FPS
    fps = int(clock.get_fps())
    texte_fps = police.render(f"FPS: {fps}", True, couleur_texte)
    fen.blit(texte_fps, (10, 10)) 
    pygame.display.flip()

pygame.quit()
