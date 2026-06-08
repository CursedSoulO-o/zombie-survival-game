import random

player_health = 100
zombie_health = 200
healing = 0

def choice_select():

    global player_health, zombie_health, healing
    player_health = max(0, min(player_health, 100))
    zombie_health = max(0, min(zombie_health, 200))

    while player_health > 0 and zombie_health > 0:

        heal_chance = random.randint(1,10)
        escape_chance = random.randint(1,10)
        z_damg = random.randint(5,15)
        p_damg = random.randint(3,20) 

        choice = int(input(" 1 = Fight ZOMBIE ⚔️ \n 2 = Heal Yourself ❤️‍🩹 \n 3 = Escape From this place 🏃‍♂️ \n Enter Your Choice : "))

        #CHOICE 1
        if choice == 1:
            player_health -= z_damg
            zombie_health -= p_damg
            player_health = max(0, player_health)
            zombie_health = max(0, zombie_health) 

            if heal_chance >=5:
                healing += 1
                print("YOU FOUND 1 HEALING")
            print(f"""    
            PLAYER 🧑‍🦱 HP: -{z_damg} Damage   ----> {player_health}
            ZOMBIE 💀 HP: -{p_damg} Damage   ----> {zombie_health}
            HEALING 💚:               ----> {healing}
            """)
            

            if player_health <=0:

                    print("=====GAMEOVER==== \n YOU RAN OUT OF HP")
                    break

            else:

                    if zombie_health <= 0:
                        print("Congratulations you killed ZOMBIE KING \n ======YOU WON=====")
                        break
        #CHOICE 2
        elif choice == 2:
            if healing > 0:
                import time

                print("HEALING", end="")

                for i in range(8):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                    
                healing -= 1
                player_health = min(player_health + 20, 100)
                print (f" HEALED!!! \n + 20HP \n Now You have {player_health} HP")
                

            else:

                    player_health -= z_damg
                    player_health = max(0, player_health) 
                    print(f"YOU HAVE {healing} HEALING ❌ \n ZOMBIE attacked You 🧟 \n Now You have {player_health} HEALTH ❤️‍🩹" )

        #CHOICE 3
        elif choice == 3:

            if escape_chance <= 3:

                print("You Escaped")
                break

            else:

                player_health -= z_damg
                player_health = max(0, player_health)
                print(f"ESCAPE FAILED!!! \n ZOMBIE Attacked you -{z_damg} HP \n Now You have {player_health} HP")      
        else:

            print("INVALID CHOICE , TRY AGAIN!!!! ❌ ")

choice_select()
