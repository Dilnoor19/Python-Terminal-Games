
import random

player_hp = 100
gold = 0
potions = 2

print("=" * 40)
print("🏰 LEGEND OF PYTHONIA")
print("=" * 40)

name = input("Hero ka naam: ")

while player_hp > 0:

    print("\n" + "-" * 40)
    print(f"❤️ HP: {player_hp}")
    print(f"🪙 Gold: {gold}")
    print(f"🧪 Potions: {potions}")
    print("-" * 40)

    print("""
1. Explore Forest
2. Drink Potion
3. Fight Dragon Boss
4. Quit
""")

    choice = input("Choose: ")

    if choice == "1":

        event = random.choice(["enemy", "treasure"])

        if event == "treasure":
            found_gold = random.randint(10, 50)
            gold += found_gold
            print(f"\n💰 You found {found_gold} gold!")

        else:
            enemy_hp = random.randint(20, 50)

            print(f"\n👹 Enemy appeared! HP = {enemy_hp}")

            while enemy_hp > 0 and player_hp > 0:

                attack = random.randint(10, 25)
                enemy_hp -= attack

                print(f"⚔️ You deal {attack} damage")

                if enemy_hp <= 0:
                    reward = random.randint(20, 60)
                    gold += reward
                    print(f"🎉 Enemy defeated!")
                    print(f"🪙 Loot: {reward} gold")
                    break

                enemy_attack = random.randint(5, 20)
                player_hp -= enemy_attack

                print(f"💥 Enemy hits for {enemy_attack}")

    elif choice == "2":

        if potions > 0:
            heal = random.randint(20, 40)
            player_hp += heal

            if player_hp > 100:
                player_hp = 100

            potions -= 1

            print(f"🧪 Restored {heal} HP")

        else:
            print("❌ No potions left!")

    elif choice == "3":

        print("\n🐉 DRAGON BOSS APPEARS!")

        dragon_hp = 150

        while dragon_hp > 0 and player_hp > 0:

            dmg = random.randint(15, 30)
            dragon_hp -= dmg

            print(f"⚔️ You hit dragon for {dmg}")
            print(f"🐉 Dragon HP: {max(dragon_hp,0)}")

            if dragon_hp <= 0:
                print("\n🏆 YOU DEFEATED THE DRAGON!")
                print("👑 KINGDOM SAVED!")
                exit()

            dragon_dmg = random.randint(10, 25)
            player_hp -= dragon_dmg

            print(f"🔥 Dragon hits for {dragon_dmg}")

    elif choice == "4":
        print("👋 Goodbye Hero!")
        break

    else:
        print("❌ Invalid Choice")

if player_hp <= 0:
    print("\n☠️ YOU DIED")
    print(f"🪙 Final Gold: {gold}")
