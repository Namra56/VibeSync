from art import tprint
import random
import songs
import pygame
import time
import datetime
def limiter(links):
    index = 0

    while index < len(links):
    
        for item in links[index:index+3]:
            print(item)

        index += 3   

        
        if index >= len(links):
            print("\n No more songs.")
            break

        
        ask = input("\nShow more? (yes/no): ")
        if ask != "yes":
            print("Stopped.")
            break

def select_service():
    print("\nSelect Streaming Service:")
    print("1) YouTube Music")
    print("2) Spotify")
    print("3) Apple Music")
    ch = input("Choose (1/2/3): ")

    if ch == "1":
        return "YouTube Music"
    elif ch == "2":
        return "Spotify"
    elif ch == "3":
        return "Apple Music"
    else:
        print("Invalid choice, defaulting to Youtube Music.")
        return "YouTube Music"

def select_mood():
    print("\nSelect Mood:")
    print("1) Energetic")
    print("2) Rage")
    print("3) Sad")
    print("4) Happy")
    ch = input("Choose (1-4): ")

    if ch == "1":
        return "Energetic"
    elif ch == "2":
        return "Rage"
    elif ch == "3":
        return "Sad"
    elif ch == "4":
        return "Happy"
    else:
        print("Invalid choice, defaulting to Energetic.")
        return "Energetic"

def select_category():
    print("\nSelect Category:")
    print("1) Singles")
    print("2) Album")
    print("3) Artist")
    ch = input("Choose (1/2/3): ")

    if ch == "1":
        return "single"
    elif ch == "2":
        return "album"
    elif ch == "3":
        return "artist"
    else:
        print("Invalid choice, defaulting to single.")
        return "single"


def mood_selector():
    print("\n--- Mood Selector ---")
    service = select_service()
    mood = select_mood()
    category = select_category()

    try:
        links = songs.curated[mood][category][service]
    except Exception:
        print("\n Data for this combination not found in songs.py.")
        print("Mood:", mood, "| Category:", category, "| Service:", service)
        return
    finally:
        print("Songs may have explicit content. Listener discretion is advised.")
    print("\n--- SONGS ---\n")
    limiter(links)

def surprise_me():
    print("\n Surprise Me Game")
    input("Press ENTER for a random combo... ")

    mood = random.choice(list(songs.curated.keys()))
    category = random.choice(list(songs.curated[mood].keys()))
    service = select_service()

    print(f"\nMood    : {mood}")
    print(f"Category: {category}")
    print(f"Service : {service}\n")

    links = songs.curated[mood][category][service]
    print("Songs may have explicit content. Listener discretion is advised.")
    limiter(links)

def mood_of_the_day():


   
    day = datetime.datetime.now().strftime("%A")

    #
    mood_map = {
        "Monday": "Energetic",
        "Tuesday": "Rage",
        "Wednesday": "Sad",
        "Thursday": "Happy",
        "Friday": "Energetic",
        "Saturday": "Happy",
        "Sunday": "Sad"
    }

    mood = mood_map[day]

    print("Today is:", day)
    print("Mood of the Day:", mood)

    
    print("\nSelect Streaming Service:")
    print("1) YouTube Music")
    print("2) Spotify")
    print("3) Apple Music")
    s = input("Enter choice (1/2/3): ")

    if s == "1":
        service = "YouTube Music"
    elif s == "2":
        service = "Spotify"
    elif s == "3":
        service = "Apple Music"
    else:
        print("Invalid choice")
        return

    category = "single"   

    try:
        links = songs.curated[mood][category][service]
    except:
        print("Songs not available for today’s mood.")
        return
    finally:
        print("Songs may have explicit content. Listener discretion is advised.")

    print("\nSongs for today's mood:\n")
    limiter(links)


def guess_the_song():
    pygame.mixer.init()

    songs = {
        "Dil nu.mp3": "Dil nu",
        "Shaayar.mp3": "Shaayar",
        "The winner takes it all.mp3": "The winner takes it all",
        "Breathless.mp3": "Breathless",
    }

    score = 0

    while True:
        for song, answer in songs.items():
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()

            guess = input("Guess the song name:(Case Sensitive!!!) ")

            if guess == answer:
                print("Correct")
                score += 1
            else:
                print("Wrong")

        print("Score:", score, "/", len(songs))

        again = input("Do you want to play again? (yes/no): ")
        if again != "yes":
            break



def main():
    tprint("VibeSync")

    while True:
        print("\n1) Mood Selector")
        print("2) Surprise Me Game")
        print("3) Mood of the Day")
        print("4) Guess the song")
        print("5) Exit")
        choice = input("Choose (1/2/3/4/5): ")

        if choice == "1":
            mood_selector()
        elif choice == "2":
            surprise_me()
        elif choice == "3":
            mood_of_the_day()
        elif choice == "4":
            guess_the_song()
        elif choice == "5":
            print("\nThanks for using VibeSync!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

