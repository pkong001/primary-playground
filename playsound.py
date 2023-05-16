import random
import time
import pygame

# Initialize Pygame
pygame.mixer.init()

# Sound choice4
s1 = './sound/ping.mp3'
s2 = './sound/click.mp3'

# Load the sound file
sound = pygame.mixer.Sound(s2)

while True:
    # Generate a random number between 1 and 60
    random_number = random.randint(40, 60)

    # Wait for the number of seconds equal to the random number
    print(f"Waiting for {random_number} seconds...")
    time.sleep(random_number)

    # Play the sound once
    print("Playing sound...")
    sound.play()
