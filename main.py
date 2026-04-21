import math
from pygame.locals import *
import random
import pygame as pg

pg.init()
screen = pg.display.set_mode((1080, 800))
bound_rect = pg.Rect(0, 0, 700, 700)
space = pg.image.load("images/space.png").convert()
space = pg.transform.scale(space, (600, 600))
space_rect = space.get_rect(center=(570, 580))
pause_surface = pg.Surface((1080, 800), pg.SRCALPHA)
explosion_sound = pg.mixer.Sound("music/explosion.mp3")
menu_music = pg.mixer.Sound("music/menu music.mp3")
pew_sound = pg.mixer.Sound("music/pew.mp3")
portal_music = pg.mixer.Sound("music/portal open.mp3")
character_grab = pg.mixer.Sound("music/character_grab.mp3")

alive_heart = pg.transform.scale(pg.image.load("images/alive heart.png"), (45, 45))
dead_heart = pg.transform.scale(pg.image.load("images/dead heart.png"), (45, 45))
half_heart = pg.transform.flip(
    pg.transform.scale(pg.image.load("images/half heart image.png"), (45, 45)),
    False,
    False
)
heart_positions = [(225, 60), (255, 60), (285, 60), (315, 60), (345, 60)]

boss_villain = pg.image.load("images/boss.png").convert_alpha()
boss_villain = pg.transform.flip(boss_villain, False, True)
boss_villain = pg.transform.scale(boss_villain, (250, 250))
boss_rect = boss_villain.get_rect(topleft=(400, 65))

villain_1 = pg.image.load("images/villain_1.png").convert_alpha()
villain_1 = pg.transform.flip(villain_1, False, True)
villain_1 = pg.transform.scale(villain_1, (35, 35))
villain_1_original = villain_1.copy()
villain_1_center = (500, 250)
villain_1_rect = villain_1.get_rect(center=villain_1_center)

villain_2 = pg.image.load("images/villain_2.png").convert_alpha()
villain_2 = pg.transform.flip(villain_2, False, True)
villain_2 = pg.transform.scale(villain_2, (35, 35))
villain_2_original = villain_2.copy()
villain_2_center = (570, 250)
villain_2_rect = villain_2.get_rect(center=villain_2_center)


player_original = pg.image.load("images/player.png").convert_alpha()
player_original = pg.transform.scale(player_original, (35, 35))
player_center = (523, 550)
player_rect = player_original.get_rect(center=player_center)

prison = pg.image.load("images/prison_prison.png").convert_alpha()
prison = pg.transform.scale(prison, (80, 80))
prison_rect = prison.get_rect()
prison_rect.center = (540, 450)
explosion = pg.image.load("images/explosion.png")
explosion = pg.transform.scale(explosion, (50, 60))
explosion_rect = explosion.get_rect()
portal = pg.image.load("images/portal.png").convert_alpha()
portal_rect = portal.get_rect()
portal_rect.center = (825, 675)
portal = pg.transform.scale(portal, (50, 50))
homescreen = pg.image.load("images/menu screen.png").convert_alpha()
howtobutton = pg.image.load("images/instruction button.png").convert_alpha()
quitbutton = pg.image.load("images/quit button.png").convert_alpha()
playbutton = pg.image.load("images/play button.png").convert_alpha()
howtoscreen = pg.image.load("images/how to screen.jpg").convert_alpha()
home1button = pg.image.load("images/home 1 button.png").convert_alpha()
quitscreen = pg.image.load("images/quit screen.png").convert_alpha()
endbutton = pg.image.load("images/end button.png").convert_alpha()
home2button = pg.image.load("images/home2button.png").convert_alpha()

homescreen = pg.transform.scale(homescreen, (1080, 800))
howtobutton = pg.transform.scale(howtobutton, (195, 40))
quitbutton = pg.transform.scale(quitbutton, (195, 40))
playbutton = pg.transform.scale(playbutton, (185, 40))
howtoscreen = pg.transform.scale(howtoscreen, (1080, 800))
home1button = pg.transform.scale(home1button, (170, 55))
quitscreen = pg.transform.scale(quitscreen, (1080, 800))
endbutton = pg.transform.scale(endbutton, (150, 50))

playbutton_rect = playbutton.get_rect(center=(540, 400))
howtobutton_rect = howtobutton.get_rect(center=(540, 475))
quitbutton_rect = quitbutton.get_rect(center=(540, 550))
howtoscreen_rect = howtoscreen.get_rect(center=(540, 400))
home1button_rect = home1button.get_rect(center=(1010, 15))
quitscreen_rect = quitscreen.get_rect(center=(540, 400))
endbutton_rect = endbutton.get_rect(center=(535, 475))
border_thickness = 10
bordered_surface = pg.Surface(
    (homescreen.get_width() + 2 * border_thickness,
     homescreen.get_height() + 2 * border_thickness),
    pg.SRCALPHA
)
bordered_surface.fill((255, 255, 255))
bordered_surface.blit(homescreen, (border_thickness, border_thickness))
homescreen_rect = bordered_surface.get_rect(center=(540, 400))

youlose = pg.image.load("images/youlosescreen.png").convert_alpha()
youlose = pg.transform.scale(youlose, (1080, 800))
youlose_rect = youlose.get_rect()
youlose_rect.center = (540, 400)
youwin = pg.image.load("images/youwinscreen.png").convert_alpha()
youwin = pg.transform.scale(youwin, (1080, 800))
youwin_rect = youwin.get_rect()
youwin_rect.center = (540, 400)
playagain = pg.image.load("images/playagainbutton.png").convert_alpha()
playagain = pg.transform.scale(playagain, (195, 45))
playagain_rect = playagain.get_rect(center=(545, 425))
homeagain = pg.image.load("images/option2button.png").convert_alpha()
homeagain = pg.transform.scale(homeagain, (195, 45))
homeagain_rect = homeagain.get_rect(center=(545, 475))

villain1_replaced = False
villain2_replaced = False
villain1_explosion = False
villain2_explosion = False

characters = []
characters_rects = []

for i in range(1, 6):
    character = pg.image.load(f"characters/character_{i}.png").convert_alpha()
    character = pg.transform.scale(character, (35, 35))
    characters.append(character)
    characters_rects.append(character.get_rect())

positions = [
    (540, 450), (535, 455), (530, 460), (525, 470), (556, 455),
]

for i, rect in enumerate(characters_rects):
    rect.center = positions[i]

last_move_time = pg.time.get_ticks()
move_interval = 5000
current_character_index = 0
moved_characters = [False] * 5


def remove_exploded_villain(villain_rect, villain_explosion):
    if villain_explosion:
        villain_rect.x, villain_rect.y = -100, -100
        villain_explosion = False
    return villain_rect, villain_explosion


def move_villains_away_from_prison(villain_rect, prison_rect, speed, min_distance):
    villain_center = villain_rect.center
    prison_center = prison_rect.center

    x_dist = villain_center[0] - prison_center[0]
    y_dist = villain_center[1] - prison_center[1]
    distance = math.sqrt(x_dist ** 2 + y_dist ** 2)

    if distance < min_distance:
        if distance != 0:
            x_dist /= distance
            y_dist /= distance

        villain_rect.x += x_dist * speed
        villain_rect.y += y_dist * speed
    else:

        move_villains(villain_rect, player_rect, speed, min_distance)


def reset_game_state():
    global current_screen, player_rect, boss_rect, villain_1_rect, villain_2_rect
    global hero_lives, villainhits1, villainhits2, character_count, characters_to_remove
    global angles, characters_rects, moved_characters, characters, velocities
    global active_villain_bullets, active_hero_bullets, villain1_replaced, villain2_replaced
    global heart_positions, game_win, game_over, current_character_index, move_interval
    global villain1_explosion, villain2_explosion

    current_screen = "game"
    player_rect = pg.Rect(525, 600, 35, 35)
    boss_rect = pg.Rect(400, 65, 250, 250)
    villain_1_rect = pg.Rect(500, 250, 35, 35)
    villain_2_rect = pg.Rect(550, 250, 35, 35)

    hero_lives = 5
    villainhits1 = 0
    villainhits2 = 0
    character_count = 0
    game_win = False
    game_over = False
    villain1_replaced = False
    villain2_replaced = False
    villain2_explosion = False
    villain1_explosion = False
    active_villain_bullets.clear()
    active_hero_bullets.clear()
    characters_to_remove = []
    angles = [0] * 11
    moved_characters = [False] * 6
    velocities = [generate_velocity(random.randint(0, 360)) for _ in range(11)]
    characters.clear()
    characters_rects.clear()

    for i in range(1, 6):
        character = pg.image.load(f"characters/character_{i}.png").convert_alpha()
        character = pg.transform.scale(character, (35, 35))
        characters.append(character)
        characters_rects.append(character.get_rect())

    positions = [
        (540, 450), (535, 455), (530, 460), (525, 470), (556, 455),
    ]

    for i, rect in enumerate(characters_rects):
        rect.center = positions[i]

    moved_characters = [False] * len(characters_rects)

    heart_positions = [(225, 60), (255, 60), (285, 60), (315, 60), (345, 60)]


def move_villains(villain_rect, player_rect, speed=1.0, min_distance=40):
    x_distance = player_rect.centerx - villain_rect.centerx
    y_distance = player_rect.centery - villain_rect.centery
    distance = math.hypot(x_distance, y_distance)

    if distance > min_distance:
        x_vel = (x_distance / distance) * speed
        y_vel = (y_distance / distance) * speed

        villain_rect.x += x_vel
        villain_rect.y += y_vel


def draw_pause():
    pause_surface.fill((128, 128, 128, 5))
    screen.blit(pause_surface, (0, 0))


def respawn_villain(villain_rect, villain_exploded, last_removed_time, respawn_delay, character_count, villainhits):
    if character_count >= 5:
        return villain_rect, villain_exploded, villainhits

    if villain_exploded:
        current_time = pg.time.get_ticks()

        if current_time - last_removed_time > respawn_delay:
            villain_rect.x = random.randint(100, 700)
            villain_rect.y = random.randint(100, 500)
            villain_exploded = False
            villainhits = 0

            return villain_rect, villain_exploded, villainhits

    return villain_rect, villain_exploded, villainhits


def generate_velocity(angle):
    rad = math.radians(angle)
    velocity_x = math.cos(rad) * random.uniform(0.5, 1.0)
    velocity_y = math.sin(rad) * random.uniform(0.5, 1.0)
    return velocity_x, velocity_y


velocities = [generate_velocity(random.randint(0, 360)) for _ in range(11)]

screen.blit(space, ((1080 - 600) // 2, (800 - 600) // 2))
pg.display.flip()

villain_bullet = pg.image.load("images/villain 1 bullet.png").convert_alpha()
hero_bullet = pg.image.load("images/hero bullet.png").convert_alpha()

bullets = pg.transform.scale(villain_bullet, (10, 10))
hero_bullets = pg.transform.scale(hero_bullet, (10, 10))

bullets_rect = bullets.get_rect()
hero_bullets_rect = hero_bullets.get_rect()

clock = pg.time.Clock()
boss_direction = True

villain_bullet_timer = {
    'villain_1': 1,
    'villain_2': 1,
    'boss': 1
}
villain_bullet_interval = 200


def calculate_direction(start, target):
    angle = math.atan2(target[1] - start[1], target[0] - start[0])
    return math.cos(angle), math.sin(angle)


def shoot_villain_bullet(villain_rect, villain_name, active_villain_bullets):
    if villain_bullet_timer[villain_name] <= 0:
        target_pos = player_rect.center
        direction = calculate_direction(villain_rect.center, target_pos)

        active_villain_bullets.append({
            'image': bullets,
            'pos': list(villain_rect.center),
            'direction': direction,
            'speed': 3
        })

        villain_bullet_timer[villain_name] = villain_bullet_interval
    else:
        villain_bullet_timer[villain_name] -= 1


active_hero_bullets = []
active_villain_bullets = []
villainhits1 = 0
villainhits2 = 0
hero_lives = 5
angles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
character_count = 0
characters_to_remove = []
game_over = False
game_win = False
current_screen = "home"
font_path = "fonts/game_over.ttf"
font2 = pg.font.Font(font_path, 55)
pause_sfx = pg.mixer.Sound("music/pause_sound.mp3")

pause = False
pause_start_time = 0
total_pause_duration = 0
last_removed_time_villain1 = 0
last_removed_time_villain2 = 0
respawn_delay = 500
running = True
while running:
    current_time = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            if not pause:
                pause = True
                pause_start_time = current_time
            else:
                pause = False
                total_pause_duration += pg.time.get_ticks() - pause_start_time
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if current_screen == "game":
                    target_pos = pg.mouse.get_pos()
                    direction = calculate_direction(player_rect.center, target_pos)
                    scaled_hero_bullet = pg.transform.scale(hero_bullet, (10, 10))
                    active_hero_bullets.append({
                        'image': scaled_hero_bullet,
                        'pos': list(player_rect.center),
                        'direction': direction,
                        'speed': 5
                    })
                elif current_screen == "home":
                    if playbutton_rect.collidepoint(mouse_pos):
                        reset_game_state()
                        menu_music.stop()
                        current_screen = "game"
                    elif howtobutton_rect.collidepoint(mouse_pos):
                        current_screen = "howto"
                    elif quitbutton_rect.collidepoint(mouse_pos):
                        current_screen = "quit"
                elif current_screen == "howto":
                    if home1button_rect.collidepoint(mouse_pos):
                        current_screen = "home"
                elif current_screen == "quit":
                    if endbutton_rect.collidepoint(mouse_pos):
                        running = False
                elif current_screen == "lose":
                    if playagain_rect.collidepoint(mouse_pos):
                        reset_game_state()
                        current_screen = "game"
                    elif homeagain_rect.collidepoint(mouse_pos):
                        reset_game_state()
                        current_screen = "home"
                elif current_screen == "win":
                    if playagain_rect.collidepoint(mouse_pos):
                        reset_game_state()
                        current_screen = "game"
                    elif homeagain_rect.collidepoint(mouse_pos):
                        reset_game_state()
                        current_screen = "home"
    if pause:
        pause_sfx.play(loops=1, fade_ms=-1)
        home2button = pg.transform.scale(home2button, (200, 100))
        home2button_rect = home2button.get_rect(topleft=(440, 300))
        escapetocontine = font2.render(f"Press ESC to Continue", True, (255, 0, 0))
        continuebutton_scaled = pg.transform.scale(escapetocontine, (325, 50))
        continuebutton_scaled_rect = continuebutton_scaled.get_rect(topleft=(400, 365))
        screen.blit(continuebutton_scaled, continuebutton_scaled_rect)
        screen.blit(home2button, home2button_rect)
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if home2button_rect.collidepoint(mouse_pos):
                current_screen = "home"
                pause = False
        draw_pause()
        pg.display.flip()
        clock.tick(60)
        continue
    if not pause:
        pause_sfx.stop()

    if current_screen == "home":
        if not pg.mixer.music.get_busy():
            menu_music.play(-1)
        screen.blit(bordered_surface, homescreen_rect)
        screen.blit(howtobutton, howtobutton_rect)
        screen.blit(quitbutton, quitbutton_rect)
        screen.blit(playbutton, playbutton_rect)
    elif current_screen == "howto":
        screen.blit(howtoscreen, howtoscreen_rect)
        screen.blit(home1button, home1button_rect)
    elif current_screen == "quit":
        screen.blit(quitscreen, quitscreen_rect)
        screen.blit(endbutton, endbutton_rect)
    elif current_screen == "lose":
        screen.blit(youlose, youlose_rect)
        screen.blit(homeagain, homeagain_rect)
        screen.blit(playagain, playagain_rect)
    elif current_screen == "win":
        screen.blit(youwin, youwin_rect)
        screen.blit(playagain, playagain_rect)
        screen.blit(homeagain, homeagain_rect)
    elif current_screen == "game":
        current_time = pg.time.get_ticks()
        screen.fill((0, 0, 0))
        screen.blit(space, ((1080 - 600) // 2, (800 - 600) // 2))
        screen.blit(boss_villain, boss_rect.topleft)
        bullets_rect.center = villain_1_rect.center
        bullets_rect.center = villain_2_rect.center
        bullets_rect.centerx = villain_1_rect.centerx + 10
        bullets_rect.centery = villain_1_rect.centery + 10
        bullets_rect.centerx = villain_2_rect.centerx + 11
        bullets_rect.centery = villain_2_rect.centery + 16
        hero_bullets_rect.centerx = player_rect.centerx
        hero_bullets_rect.centery = player_rect.centery
        for i, position in enumerate(heart_positions):
            if hero_lives >= i + 1:
                screen.blit(alive_heart, position)
            elif hero_lives == i + 0.5:
                screen.blit(half_heart, position)
            elif hero_lives == 0:
                game_over = True
                current_screen = "lose"
            else:
                screen.blit(dead_heart, position)
        keys = pg.key.get_pressed()
        move_speed = 5
        if keys[K_w] and player_rect.top > 250:
            new_position = player_rect.move(0, -5)
            if not new_position.colliderect(prison_rect):
                player_rect = new_position
        if keys[K_s] and player_rect.bottom < 690:
            new_position = player_rect.move(0, 5)
            if not new_position.colliderect(prison_rect):
                player_rect = new_position
        if keys[K_a] and player_rect.left > 249:
            new_position = player_rect.move(-5, 0)
            if not new_position.colliderect(prison_rect):
                player_rect = new_position
        if keys[K_d] and player_rect.right < 835:
            new_position = player_rect.move(5, 0)
            if not new_position.colliderect(prison_rect):
                player_rect = new_position
        pos = pg.mouse.get_pos()
        x_dist = pos[0] - player_rect.centerx
        y_dist = -(pos[1] - player_rect.centery)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        player = pg.transform.rotate(player_original, angle - 90)
        player_rect_rotated = player.get_rect(center=player_rect.center)

        move_villains(villain_1_rect, player_rect, speed=1, min_distance=150)
        move_villains(villain_2_rect, player_rect, speed=1, min_distance=150)

        x_dist_villain_1 = player_rect.centerx - villain_1_rect.centerx
        y_dist_villain_1 = -(player_rect.centery - villain_1_rect.centery)
        angle_villain_1 = math.degrees(math.atan2(y_dist_villain_1, x_dist_villain_1))
        villain_1 = pg.transform.rotate(villain_1_original, angle_villain_1 + 90)
        villain_1_rect_rotated = villain_1.get_rect(center=villain_1_rect.center)

        x_dist_villain_2 = player_rect.centerx - villain_2_rect.centerx
        y_dist_villain_2 = -(player_rect.centery - villain_1_rect.centery)
        angle_villain_2 = math.degrees(math.atan2(y_dist_villain_2, x_dist_villain_2))
        villain_2 = pg.transform.rotate(villain_2_original, angle_villain_2 + 90)
        villain_2_rect_rotated = villain_2.get_rect(center=villain_2_rect.center)
        move_villains_away_from_prison(villain_1_rect, prison_rect, speed=1, min_distance=150)
        move_villains_away_from_prison(villain_2_rect, prison_rect, speed=1, min_distance=150)

        if boss_direction:
            boss_rect = boss_rect.move(1, 0)
        else:
            boss_rect = boss_rect.move(-1, 0)

        if boss_rect.right >= 865 or boss_rect.left <= 225:
            boss_direction = not boss_direction

        for i in range(len(angles)):
            if i % 2 == 0:
                angles[i] += (i + 1) * 0.2

        rotated_characters = []
        rotated_rects = []

        for i in range(len(characters)):
            rotated_character = pg.transform.rotate(characters[i], angles[i])
            rotated_rect = rotated_character.get_rect()
            rotated_rect.center = characters_rects[i].center
            rotated_characters.append(rotated_character)
            rotated_rects.append(rotated_rect)

        current_time = pg.time.get_ticks()
        for i in range(len(characters)):
            if not moved_characters[i] and current_time - last_move_time >= move_interval:
                moved_characters[i] = True
                last_move_time = current_time

        characters_to_remove = []
        for i in range(len(characters)):
            if moved_characters[i]:
                characters_rects[i].x += velocities[i][0]
                characters_rects[i].y += velocities[i][1]

                if rotated_rects[i].colliderect(player_rect):
                    character_grab.play()
                    character_count += 1
                    characters_to_remove.append(characters_rects[i])
                    print(f"Character count updated: {character_count}")

                if not bound_rect.colliderect(characters_rects[i]):
                    game_over = True
                    reset_game_state()
                    current_screen = "lose"

        for rect in characters_to_remove:
            index = characters_rects.index(rect)
            characters_rects.pop(index)
            characters.pop(index)
            angles.pop(index)
            velocities.pop(index)
            moved_characters.pop(index)
            rotated_characters.pop(index)
            rotated_rects.pop(index)

        characters_to_remove.clear()

        score_text = font2.render(f"Character Count: {character_count}", True, (255, 255, 255))
        screen.blit(score_text, (625, 70))

        for i in range(len(rotated_characters)):
            screen.blit(rotated_characters[i], rotated_rects[i].topleft)

        screen.blit(prison, prison_rect)
        screen.blit(player, player_rect_rotated)
        if villain1_explosion:
            pew_sound.stop()
        else:
            for bullet in active_villain_bullets[:]:
                bullet['pos'][0] += bullet['direction'][0] * bullet['speed']
                bullet['pos'][1] += bullet['direction'][1] * bullet['speed']

                bullet_rect = bullet['image'].get_rect(center=(int(bullet['pos'][0]), int(bullet['pos'][1])))

                if bullet_rect.colliderect(player_rect):
                    hero_lives -= 0.5
                    active_villain_bullets.remove(bullet)
                elif bullet['pos'][0] < 0 or bullet['pos'][0] > 800 or bullet['pos'][1] < 0 or bullet['pos'][1] > 800:
                    active_villain_bullets.remove(bullet)

                screen.blit(bullet['image'], bullet_rect.topleft)

                shoot_villain_bullet(villain_1_rect, 'villain_1', active_villain_bullets)
                pew_sound.play()

        if boss_rect.colliderect(space_rect):
            shoot_villain_bullet(boss_rect, 'boss', active_villain_bullets)

        if villain2_explosion:
            pew_sound.stop()
        else:
            for bullet in active_villain_bullets[:]:
                bullet['pos'][0] += bullet['direction'][0] * bullet['speed']
                bullet['pos'][1] += bullet['direction'][1] * bullet['speed']

                bullet_rect = bullet['image'].get_rect(center=(int(bullet['pos'][0]), int(bullet['pos'][1])))

                if bullet_rect.colliderect(player_rect):
                    hero_lives -= 0.5
                    active_villain_bullets.remove(bullet)
                elif bullet['pos'][1] < 0 or bullet['pos'][1] > 680:
                    active_villain_bullets.remove(bullet)
                elif bullet['pos'][1] < 0 or bullet['pos'][1] > 680:
                    active_villain_bullets.remove(bullet)

                screen.blit(bullet['image'], bullet_rect.topleft)

                shoot_villain_bullet(villain_2_rect, 'villain_2', active_villain_bullets)

        for bullet in active_hero_bullets[:]:
            bullet['pos'][0] += bullet['direction'][0] * bullet['speed']
            bullet['pos'][1] += bullet['direction'][1] * bullet['speed']
            screen.blit(bullet['image'], bullet['pos'])
            bullet_rect = bullet['image'].get_rect(center=(int(bullet['pos'][0]), int(bullet['pos'][1])))

            if bullet_rect.colliderect(villain_1_rect) or bullet_rect.colliderect(villain_2_rect):
                if bullet_rect.colliderect(villain_1_rect):
                    villainhits1 += 1
                if bullet_rect.colliderect(villain_2_rect_rotated):
                    villainhits2 += 1
                active_hero_bullets.remove(bullet)

        if villainhits1 >= 10 and not villain1_explosion:
            explosion_sound.play()
            villain1_explosion = True
            last_explosion_time_villain1 = pg.time.get_ticks()

        if villainhits2 >= 10 and not villain2_explosion:
            explosion_sound.play()
            villain2_explosion = True
            last_explosion_time_villain2 = pg.time.get_ticks()

        explosion_duration = 300

        if villain1_explosion:
            time_since_explosion1 = current_time - last_explosion_time_villain1
            if time_since_explosion1 >= explosion_duration:
                villain_1_rect, villain1_explosion, villainhits1 = respawn_villain(
                    villain_1_rect, villain1_explosion, last_removed_time_villain1, respawn_delay,
                    villainhits1, character_count)

        if villain2_explosion:
            time_since_explosion2 = current_time - last_explosion_time_villain2
            if time_since_explosion2 >= explosion_duration:
                villain_2_rect, villain2_explosion, villainhits2 = respawn_villain(
                    villain_2_rect, villain2_explosion, last_removed_time_villain2, respawn_delay,
                    villainhits2, character_count)

        if villain1_explosion:
            screen.blit(explosion, villain_1_rect)
        else:
            screen.blit(villain_1, villain_1_rect)

        if villain2_explosion:
            screen.blit(explosion, villain_2_rect)
        else:
            screen.blit(villain_2, villain_2_rect_rotated)

        if game_win:
            screen.blit(portal, portal_rect)
            portal_music.play()
            if portal_rect.colliderect(player_rect):
                portal_music.stop()
                current_screen = "win"
        if character_count == 5:
            game_win = True

    pg.display.flip()

    clock.tick(60)

pg.quit()

