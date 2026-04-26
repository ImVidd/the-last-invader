# Developer Documentation

Developer Documentation - The Last Invader

Version: 1.0

Authors: Samuel Florez Garcia & Kimora Robinson

Last Updated: April 2026

---
 
Table of Contents

1. Project Overview	

2. Project Structure	

3. Dependencies	

4. Game Architecture	

5. Core Functions	

6. Game States

7. Game Objects	

8. Game Logic Flow	

9. Known Limitations	

---
 
1. Project Overview

The Last Invader is a 2D top-down space shooter built entirely in Python using the Pygame library. The entire game runs from a single file, main.py, which handles all game logic, rendering, input handling, and audio. The game was developed using PyCharm and is compatible with macOS, Windows, and Linux.

---
 
2. Project Structure

the-last-invader/

- main.py               # Main and only game file

- requirements.txt      # Python dependencies

- images/               # All image assets (sprites, backgrounds, buttons, screens)

- music/                # All audio files (sound effects and background music)

- characters/           # Hostage character sprites (character_1.png to character_5.png)

- fonts/                # Custom font files used for in-game text

- docs/                 # Documentation files
 
---

3. Dependencies

The game requires Python 3.7 or higher and only one external library:

pygame

Install it with:

pip3 install pygame

All other modules used (math, random) are part of the Python standard library and require no installation.

---
 
4. Game Architecture

The game follows a single-file, event-driven architecture typical of small Pygame projects. The structure is:

Initialization - Pygame is initialized and all assets (images, sounds, fonts) are loaded into memory at the start of the program before the game loop begins. This avoids performance issues from loading assets during gameplay.

Main Game Loop - The entire game runs inside a while running loop that executes 60 times per second (60 FPS), controlled by clock.tick(60). Each iteration of the loop handles three things in order: event processing, game state updates, and rendering.

Screen State System - Rather than using separate scene classes, the game uses a single string variable called current_screen to track which screen is active. The main loop checks this variable on every frame and renders the appropriate content. Possible values are "home", "game", "howto", "quit", "lose", and "win".

---
 
5. Core Functions

move_villains(villain_rect, player_rect, speed, min_distance)

Moves a villain spaceship toward the player character each frame. It calculates the vector between the villain and the player using math.hypot, normalizes it, and moves the villain along that direction at the given speed. Movement stops when the villain reaches the minimum distance from the player to avoid overlapping.

move_villains_away_from_prison(villain_rect, prison_rect, speed, min_distance)

Prevents villains from getting stuck inside the prison object in the center of the screen. If a villain gets too close to the prison, this function pushes it away in the opposite direction. If the villain is far enough from the prison, it falls back to the standard move_villains behavior.

shoot_villain_bullet(villain_rect, villain_name, active_villain_bullets)

Handles bullet firing for a specific villain. It checks an internal timer for that villain and, when the timer reaches zero, calculates the direction toward the player and appends a new bullet dictionary to the active_villain_bullets list. Each bullet is stored as a dictionary containing its image, current position, direction vector, and speed.

calculate_direction(start, target)

A utility function that takes two positions and returns a normalized direction vector as a tuple of (cos, sin) values using math.atan2. Used by both villain and hero bullet systems to aim shots.

respawn_villain(villain_rect, villain_exploded, last_removed_time, respawn_delay, character_count, villainhits)

Handles villain respawning after being destroyed. If the villain has exploded and enough time has passed (defined by respawn_delay), it repositions the villain at a random location on screen and resets its hit counter. Respawning stops once all 5 hostages have been rescued (character_count >= 5).

reset_game_state()

Resets all game variables back to their starting values. Called when the player starts a new game or restarts after a win or loss. This includes resetting lives, hit counters, bullet lists, character positions, angles, velocities, and the current screen.

generate_velocity(angle)

Generates a random velocity vector for a hostage character based on a given angle in degrees. Used to give each hostage a unique drift direction when they begin moving away from the prison.

draw_pause()

Renders a semi-transparent grey overlay on the screen when the game is paused, giving the visual effect of the game being frozen behind the pause menu.

--- 
 
6. Game States

The game uses the variable current_screen to manage which state is active. Here is how each state works:

"home" - Displays the main menu with Play, Instructions, and Quit buttons. Background music loops here. Mouse click events are checked against button rectangles to handle navigation.

"howto" - Displays the How to Play screen image. A home button in the top right returns the player to the main menu.

"quit" - Displays a quit confirmation screen with an End button that closes the game.

"game" - The main gameplay state. All game logic runs here including player movement, villain AI, bullet updates, hostage movement, collision detection, scoring, and win/lose condition checks.

"lose" - Displays the You Lose screen with Play Again and Home buttons.

"win" - Displays the You Win screen with Play Again and Home buttons.

"pause" - Handled separately from current_screen using a boolean variable called pause. When pause is True, the game skips all update logic and renders the pause overlay instead.

---
 
7. Game Objects

All game objects are represented using Pygame's Rect class for position and collision detection, paired with a separately loaded image surface for rendering. Below are the main objects:

Player - Controlled by WASD keys. Rotates to face the mouse cursor each frame using math.atan2. Movement is bounded to a defined play area and blocked by the prison rectangle.

Villain 1 and Villain 2 - Two small enemy spaceships that chase the player. Each has its own hit counter (villainhits1, villainhits2). At 10 hits, an explosion animation plays and the villain respawns after a short delay.

Boss - A large enemy that moves horizontally across the top of the screen by incrementing or decrementing its x position each frame. Direction reverses when it reaches the left or right boundary. The boss shoots bullets when its rectangle overlaps with the space background area.

Prison - A static object in the center of the screen. Hostages start here and drift outward over time. The player cannot move through it.

Hostages - Five character sprites loaded from the characters/ folder. They start stacked on the prison and begin drifting in random directions after a set time interval. They rotate as they move. If the player's rectangle collides with a hostage, it is collected and the character count increases. If a hostage leaves the game boundary, the game ends.

Portal - Becomes visible once all 5 hostages are collected. Positioned in the bottom right of the play area. If the player collides with it, the win screen is triggered.

Bullets - Both hero and villain bullets are stored as lists of dictionaries. Each dictionary holds the bullet image, current x/y position as a list, direction vector, and speed. Bullets are moved each frame by adding their direction multiplied by their speed to their position.

---
 
8. Game Logic Flow

The following describes what happens on each frame during the "game" state:

1.	The screen is cleared and the space background is drawn

2.	The boss is drawn and its horizontal position is updated

3.	Player input is read from the keyboard and the player rectangle is moved accordingly

4.	The player sprite is rotated to face the mouse cursor and drawn

5.	Both villain spaceships are moved toward the player and rotated to face the player

6.	Villain bullet timers are decremented and new bullets are fired when timers expire

7.	All active villain bullets are moved and checked for collision with the player

8.	All active hero bullets are moved and checked for collision with villains

9.	Villain hit counts are checked - if a villain reaches 10 hits, its explosion sequence begins

10.	Villain respawn timers are checked and villains are repositioned if enough time has passed

11.	Hostage movement timers are checked and hostages begin drifting after the interval expires

12.	Hostage positions are updated and checked for collision with the player and game boundaries

13.	The portal is drawn if all hostages are collected, and checked for collision with the player

14.	Hearts are drawn based on the current hero lives value

15.	The character count score is rendered in the top right

16.	The display is updated with pg.display.flip()

---
 
9. Known Limitations

Single file structure - The entire game is contained in one file. For a larger project this would be refactored into separate modules for game objects, screens, and utilities.

No save system - There is no way to save progress. Each session starts fresh.

Bullet list duplication - The villain bullet update loop runs twice in the main loop (once for villain 1 and once for villain 2), which can cause bullets to move at double speed or be processed twice per frame. This is a known bug from the original development.

Fixed resolution - The game window is fixed at 1080x800 and cannot be resized.

Asset paths are relative - All assets are loaded using relative paths, so the game must be run from inside the project folder or it will crash on startup.


