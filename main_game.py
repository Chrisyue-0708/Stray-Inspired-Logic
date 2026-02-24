python
# ==========================================
# STRAY MINI-ENGINE: SYSTEM INTEGRATION
# ==========================================
# Developed by: Chrisyue-0708 (Yr 10, UTC Reading)
# Purpose: Connecting Cat Movement with B-12 Scanner
# ==========================================

from stray_logic import StrayGameLogic
from b12_system import B12Drone
import time

class StrayMissionRunner:
    def __init__(self):
        # Initialize the core gameplay actors
        self.ginger = StrayGameLogic("Ginger")
        self.b12 = B12Drone()
        self.mission_active = True

    def start_mission(self):
        print(">>> MISSION START: Sector 4 Gatehouse Escape")
        time.sleep(1)

        # STEP 1: POSITIONING
        # Cat moves to the trigger zone at Position 10
        print("\n[PHASE 1]: Navigating to the Scanner Range...")
        self.ginger.move_to_target(10)

        # STEP 2: TRIGGER LOGIC
        # Once the cat reaches the gate, B-12 is automatically deployed
        if self.ginger.position >= 10:
            print("\n[PHASE 2]: Target Reached. Deploying B-12 Tactical Scanner...")
            time.sleep(1)
            self._execute_scanning_sequence()
        else:
            print("\n[ALERT]: Cat failed to reach the objective.")

    def _execute_scanning_sequence(self):
        # Trigger the B-12 module
        self.b12.scan_area()
        
        # FINAL LOGIC: Mission outcome based on B-12 battery
        if self.b12.battery_level > 0:
            print("\n>>> MISSION SUCCESS: Data logged. Sector Gate Unlocked.")
        else:
            print("\n>>> MISSION FAILED: B-12 power depleted.")

if __name__ == "__main__":
    # Create the mission instance and run
    game_controller = StrayMissionRunner()
    game_controller.start_mission()
