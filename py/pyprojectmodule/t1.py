"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

"""
import random
import math
import os
import arcade

STARTING_ASTEROID_COUNT = 3
SCALE = 0.5
OFFSCREEN_SPACE = 300
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid Smasher"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE


class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """
    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class ShipSprite(arcade.Sprite):
    """
    Sprite that represents our space ship.

    Derives from arcade.Sprite.
    """
    def __init__(self, filename, scale):
        """ Set up the space ship. """

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.drag = 0.05
        self.respawning = 0

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):
        """
        Called when we die and need to make a new ship.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0

        """ Call the parent class. """
        super().update()


class AsteroidSprite(TurningSprite):
    """ Asteroid Sprite """
    def update(self):
        super().update()

        # If the sprite moves off-screen, move it to the other side
        if self.right < 0:
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Initialize the game """

        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.BLACK)

        # Sprite lists
        self.ship_list = None
        self.bullet_list = None
        self.asteroid_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.player_sprite = ShipSprite(":resources:images/space_shooter/playerShip1_orange.png", SCALE)

        # Sounds
        self.laser_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        #self.death_sound = arcade.load_sound("sounds/death.ogg")

        # Set up the walls
        self.physics_engine = None
        self.walls = None

        # Set the game state
        self.game_state = "playing"

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.ship_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = ShipSprite(":resources:images/space_shooter/playerShip1_orange.png", SCALE)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.ship_list.append(self.player_sprite)

        # Create asteroids
        for _ in range(STARTING_ASTEROID_COUNT):
            asteroid = AsteroidSprite(":resources:images/space_shooter/meteorGrey_big1.png", SCALE)

            # Position the asteroid randomly around the edges
            asteroid.center_x = random.choice([0, SCREEN_WIDTH])
            asteroid.center_y = random.uniform(0, SCREEN_HEIGHT)
            asteroid.angle = random.uniform(0, 360)

            # Apply a random speed
            asteroid.change_x = random.uniform(-1, 1) * 2
            asteroid.change_y = random.uniform(-1, 1) * 2

            self.asteroid_list.append(asteroid)

        # Set up the walls
        self.walls = arcade.SpriteList()
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SCALE)
        wall.center_x = SCREEN_WIDTH / 2
        wall.center_y = 5
        self.walls.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SCALE)
        wall.center_x = SCREEN_WIDTH / 2
        wall.center_y = SCREEN_HEIGHT - 5
        self.walls.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SCALE)
        wall.center_x = 5
        wall.center_y = SCREEN_HEIGHT / 2
        self.walls.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SCALE)
        wall.center_x = SCREEN_WIDTH - 5
        wall.center_y = SCREEN_HEIGHT / 2
        self.walls.append(wall)

        # Set up the physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.walls)

        # Set the score to 0
        self.score = 0

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites
        self.asteroid_list.draw()
        self.ship_list.draw()
        self.bullet_list.draw()

        # Draw the score on the screen
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.thrust = 0.1
        elif key == arcade.key.DOWN:
            self.player_sprite.thrust = -0.1
        elif key == arcade.key.LEFT:
            self.player_sprite.change_angle = 3
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -3
        elif key == arcade.key.SPACE:
            if self.game_state == "playing":
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SCALE)
                bullet.angle = self.player_sprite.angle
                bullet.change_x = -math.sin(math.radians(bullet.angle)) * 5
                bullet.change_y = math.cos(math.radians(bullet.angle)) * 5
                bullet.center_x = self.player_sprite.center_x
                bullet.center_y = self.player_sprite.center_y
                self.bullet_list.append(bullet)
                arcade.play_sound(self.laser_sound)

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.thrust = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Update the player animation
        self.player_sprite.update()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.bullet_list.update()
        self.asteroid_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:
            asteroids = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            # If the bullet hit an asteroid, remove the bullet and the asteroid
            if len(asteroids) > 0:
                bullet.remove_from_sprite_lists()

            for asteroid in asteroids:
                asteroid.remove_from_sprite_lists()
                arcade.play_sound(self.hit_sound)
                self.score += 1

        # Update the physics engine
        self.physics_engine.update()

        # Generate new asteroids
        if len(self.asteroid_list) < STARTING_ASTEROID_COUNT:
            asteroid = AsteroidSprite("images/asteroid.png", SCALE)

            # Position the asteroid randomly around the edges
            asteroid.center_x = random.choice([0, SCREEN_WIDTH])
            asteroid.center_y = random.uniform(0, SCREEN_HEIGHT)
            asteroid.angle = random.uniform(0, 360)

            # Apply a random speed
            asteroid.change_x = random.uniform(-1, 1) * 2
            asteroid.change_y = random.uniform(-1, 1) * 2

            self.asteroid_list.append(asteroid)

        # Check for collisions between the player and asteroids
        if self.game_state == "playing":
            player_hit = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
            if len(player_hit) > 0:
                self.game_state = "game_over"
                self.player_sprite.respawning = 1
                arcade.play_sound(self.death_sound)

    def reset_game(self):
        """ Reset the game state """
        self.setup()
        self.game_state = "playing"

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if self.game_state == "game_over":
            self.reset_game()

    def on_resize(self, width, height):
        """ Called whenever the window is resized. """
        super().on_resize(width, height)
        arcade.set_viewport(0, width, 0, height)

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
