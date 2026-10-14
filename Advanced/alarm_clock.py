# python alarm clock -

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm_sound.mp3"  # Replace with the path to your alarm sound file also-
    # add in project folder
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")  # Print current time on the same line

        if current_time == alarm_time:
            print("\nAlarm ringing!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)  # Play the sound in a loop

            while pygame.mixer.music.get_busy():
                time.sleep(1)  # Wait for the sound to finish playing
                
            is_running = False  # Stop the loop after the alarm rings

        time.sleep(1)  # Check every second - ai have written this code in a way that it will check the time every second and if the current time matches the alarm time, it will play the alarm sound. You can uncomment the lines to enable the alarm functionality.


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in format (HH:MM:SS): ")
    set_alarm(alarm_time)
