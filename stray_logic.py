import time

class StrayGameLogic:
    def __init__(self, cat_name="Ginger"):
        self.cat_name = cat_name
        self.position = 0
        self.energy = 100
        self.inventory = []
        self.door_locked = True
        self.target_door_pos = 10 # The door is located at Position 10

    def move_to_target(self, distance):
        print(f"\n--- MISSION: Reach the Sector Gate ---")
        for step in range(1, distance + 1):
            if self.energy <= 0:
                print(f"[{self.cat_name}] is exhausted. Need to find a place to nap... 💤")
                break
            
            self.position += 1
            self.energy -= 5
            print(f"Step {self.position}/{distance}: " + "." * self.position + "🐾 (Energy: {self.energy}%)")
            time.sleep(0.3)

            # Logic Check: Did we reach the door?
            if self.position == self.target_door_pos:
                print("\n[B-12]: 'System detected. We have reached the gate.'")
                self.interact_with_door()
                break

    def interact_with_door(self):
        print(f"[{self.cat_name}] is scratching the door... [SCRATCHING SOUND]")
        time.sleep(1)
        
        if self.door_locked:
            print("[B-12]: 'This door requires a keycard. Searching for signals...'")
            # Simulate finding/having a keycard
            self.inventory.append("Sector_Keycard")
            
            if "Sector_Keycard" in self.inventory:
                print("[B-12]: 'Keycard found! Decrypting security code...'")
                time.sleep(1.5)
                self.door_locked = False
                print("STATUS: DOOR OPENED [|||       |||]")
                print(f"[{self.cat_name}] proceeds to the next level.")

# --- Run the Integrated Simulation ---
stray_sim = StrayGameLogic("Stray Cat")
stray_sim.move_to_target(15) # Cat tries to move 15 steps