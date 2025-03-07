import pygame
import random

"""1. Feladat
Egészítsd ki a "Példák" fülön elérhető második kódot úgy,
hogy a 'b' billentyű lenyomására kék (blue), az 'y' gomb
lenyomására sárga (yellow) legyen az ablak háttérszíne,
és az ablak címe mutassa az éppen aktuális háttérszín RGB
értékét ilyen módon: "Az ablak háttérszínének RGB értéke:
(0, 255, 0)"""

"""
2. Feladat
Módosítsd a fenti programot úgy, hogy egy szótár típusú változó tárolja kulcsként
 a billenytű kódját, és a hozzátartozó érték pedig egy RGB kódót tartalamzó konstans legyen!
 Legalább 4 különböző háttérszínt lehessen választani!"""

pygame.init()


# Színek RGB formátumban
szinek = {
    pygame.K_b : [0, 0, 255],
    pygame.K_y : [255, 255, 0],
    pygame.K_r : [255, 0, 0],
    pygame.K_g : [0, 255, 0],
    pygame.K_w : [255, 255, 255],
    pygame.K_a : [0, 0, 0] 
}



clock = pygame.time.Clock()

# Kezdeti szín
szin = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# HARDVERES GYORSÍTÁS ENGEDÉLYEZÉSE
screen = pygame.display.set_mode((600, 300), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)

mennyen_e = True
valtozott = True  # Csak akkor rajzolunk, ha szükséges

while mennyen_e:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mennyen_e = False
        elif event.type == pygame.KEYDOWN:
            if event.key in szinek.keys():
                szin = szinek[event.key]
            valtozott = True  # Beállítjuk, hogy frissíteni kell az ablakot

    # Csak akkor frissítünk, ha változott a szín
    if valtozott:
        screen.fill(szin)
        pygame.display.set_caption(f"Az ablak háttérszínének RGB értéke: {tuple(szin)}")
        pygame.display.flip()
        valtozott = False  # Visszaállítjuk, hogy ne frissítsen feleslegesen
        print(f"FPS:{clock.get_fps():.0f} {tuple(szin)}")

    pygame.event.clear()  # Tisztítja az eseménylistát, csökkentve a terhelést
    clock.tick(10)  # 10 FPS-re limitáljuk, hogy ne pörögjön feleslegesen a CPU
    

pygame.quit()
