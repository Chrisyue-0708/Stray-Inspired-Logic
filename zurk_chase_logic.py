python
import math
import time

class Entity:
    def __init__(self, name, x, y, speed):
        self.name = name
        self.x, self.y = x, y
        self.speed = speed

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Zurk(Entity):
    def __init__(self, x, y):
        super().__init__("Zurk", x, y, speed=3.2)
        self.is_alive = True

    def chase(self, cat):
        if not self.is_alive: return
        
        # Vector Math: Direction toward the cat
        dist = self.distance_to(cat)
        if dist > 0.2:
            self.x += ((cat.x - self.x) / dist) * self.speed
            self.y += ((cat.y - self.y) / dist) * self.speed
            
    def explode(self):
        self.is_alive = False
        print(f"[*] {self.name} burst into yellow goo!")

class Defluxor:
    def __init__(self):
        self.range = 8.0        # Effective radius
        self.heat_level = 0.0   # 0.0 to 100.0
        self.is_overheated = False

    def use(self, swarm, cat_pos):
        if self.is_overheated:
            print("[!] Defluxor overheated! Waiting to cool down...")
            return

        self.heat_level += 15.0 # Heat up while using
        if self.heat_level >= 100.0:
            self.is_overheated = True
            self.heat_level = 100.0

        # Logic: Kill Zurks within range
        for zurk in swarm:
            if zurk.is_alive and zurk.distance_to(cat_pos) <= self.range:
                zurk.explode()

    def cool_down(self):
        if self.heat_level > 0:
            self.heat_level -= 5.0
        if self.heat_level <= 0:
            self.is_overheated = False
            self.heat_level = 0

class StrayCat(Entity):
    def __init__(self, x, y):
        super().__init__("Stray", x, y, speed=5.5)
        self.defluxor = Defluxor()

    def update_status(self, swarm):
        # Every frame, the cat moves and the light cools down slightly
        self.defluxor.cool_down()
        for zurk in swarm:
            zurk.chase(self)

# --- Simulation Logic ---
cat = StrayCat(0, 0)
# Spawn a small swarm around the cat
zurk_swarm = [Zurk(10, 5), Zurk(-5, 8), Zurk(3, -12)]

print(f"--- Action Sequence: Defluxor Engaged ---")
for frame in range(1, 6):
    print(f"\nFrame {frame}: Cat is at ({cat.x:.1f}, {cat.y:.1f}) | Heat: {cat.defluxor.heat_level}%")
    
    # 1. Cat moves away
    cat.x += 2.0; cat.y += 2.0
    
    # 2. Zurks chase
    cat.update_status(zurk_swarm)
    
    # 3. Use UV Light in Frame 2 and 3
    if frame in [2, 3]:
        print(">>> LIGHT ON! <<<")
        cat.defluxor.use(zurk_swarm, cat)

print("\n--- Final Status ---")
alive_count = sum(1 for z in zurk_swarm if z.is_alive)
print(f"Zurks remaining: {alive_count}")
