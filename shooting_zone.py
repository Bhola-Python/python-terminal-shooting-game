import random

print("""
🎮====================================🎮
        🔥 SHOOTING STARTS 🔥
🎮====================================🎮
""")

health = 40


class Battle:

    def __init__(self, health):
        self.health = health

    def player(self):
        self.sharif_health = self.health
        self.jojo_health = self.health
        self.sharif_bullet = random.randint(1, 6)
        self.jojo_bullet = random.randint(1, 6)

    def status(self):
        print("\n🎯========== BATTLE STATS ==========")
        print(f"🤠 Sharif")
        print(f"❤️ Health : {self.sharif_health}")
        print(f"🔫 Bullet Damage : {self.sharif_bullet}")

        print()

        print(f"😎 JOJO")
        print(f"❤️ Health : {self.jojo_health}")
        print(f"🔫 Bullet Damage : {self.jojo_bullet}")
        print("===================================\n")

    def fight(self):

        while True:

            self.sharif_luck = int(input("🎲 Enter your Luck Number (1-6): "))
            if self.sharif_luck > 6 or self.sharif_luck < 1:
                print("""
                        💥━━━━━━━━━━━━━━━━━━━━━━💥
                        🚫 INVALID MOVE!
                        🎯 Your Luck Power is too high!
                        🎲 Enter a value from 1️⃣ to 6️⃣
                        💥━━━━━━━━━━━━━━━━━━━━━━💥
                    """)
                break
            
            self.jojo_luck = random.randint(1, 6)

            print(f"\n🎲 Sharif rolled : {self.sharif_luck}")
            print(f"🎲 JOJO rolled   : {self.jojo_luck}\n")

            if self.jojo_luck > self.sharif_luck:
                self.sharif_health -= self.jojo_bullet

                print("💥 JOJO attacks Sharif!")
                print(f"❤️ Sharif Health: {self.sharif_health}")

                self.status()

            elif self.sharif_luck > self.jojo_luck:
                self.jojo_health -= self.sharif_bullet

                print("💥 Sharif attacks JOJO!")
                print(f"❤️ JOJO Health: {self.jojo_health}")

                self.status()

            else:
                print("🤝 Both players got the same luck!")
                print("⚔️ Nobody takes damage!")

                self.status()

            if self.sharif_health <= 0:
                print("""
🏆==========================
🎉 JOJO WINS!
💀 Sharif has fallen.
==========================
""")
                break

            elif self.jojo_health <= 0:
                print("""
🏆==========================
🎉 SHARIF WINS!
💀 JOJO has fallen.
==========================
""")
                break


game = Battle(health)
game.player()
game.status()
game.fight()