python
import time
import random

class B12Drone:
    def __init__(self):
        self.drone_name = "B-12"
        self.battery_level = 100
        # Database of known entities in the Dead City
        self.entity_database = {
            "Companion": {"status": "FRIENDLY", "action": "Initiate translation..."},
            "Zurk": {"status": "DANGER", "action": "ACTIVATE DEFENSE SYSTEM! ⚠️"},
            "Sentinel": {"status": "HOSTILE", "action": "Stay in the shadows..."},
            "Cat": {"status": "ALLY", "action": "Purr detected. Follow the lead."}
        }

    def scan_area(self):
        print(f"\n[{self.drone_name}]: 'Scanning surroundings for biological and mechanical signatures...'")
        time.sleep(1.5)
        
        # Simulating random entities appearing near the cat
        detected_entities = ["Companion", "Zurk", "Companion", "Cat"]
        target = random.choice(detected_entities)
        
        print(f"[{self.drone_name}]: 'Target Identified: {target}'"j
             )
        self._analyze_target(target)

    def _analyze_target(self, entity_name):
        data = self.entity_database.get(entity_name)
        
        if data["status"] == "DANGER":
            print(f"!!! WARNING !!! Status: {data['status']}")
            print(f"System Message: {data['action']}")
            self._trigger_alarm()
        elif data["status"] == "FRIENDLY":
            print(f"Status: {data['status']}")
            print(f"B-12 Message: {data['action']}")
            print("'Hello, friend. Do you have any memories for me?'")
        else:
            print(f"Status: {data['status']} | Action: {data['action']}")

    def _trigger_alarm(self):
        for _ in range(3):
            print("🚨 [BEEP-BEEP-BEEP] 🚨")
            time.sleep(0.5)
        print("Scanners offline. Evade immediately!")

# --- Simulation Start ---
my_drone = B12Drone()
my_drone.scan_area()
