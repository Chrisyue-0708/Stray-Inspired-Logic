python
import math

class VerticalNavigator:
    """
    Simulates the core parkour logic of Stray: 
    Detecting jumpable surfaces in a vertical urban environment.
    """
    
    def __init__(self):
        # Constraints based on feline physics
        self.max_jump_height = 2.5    # Meters (Y-axis)
        self.max_jump_distance = 3.5  # Meters (Horizontal)
        self.min_surface_width = 0.4  # Minimum width required for paws
        self.current_target = None

    def scan_environment(self, cat_pos, environment_data):
        """
        Performs a 'Raycast-style' sweep to find valid jump targets.
        """
        print(f"\n[B-12 System]: Scanning vertical sector at {cat_pos}...")
        valid_ledges = []

        for obj in environment_data:
            # 1. Calculate relative distance (Horizontal & Vertical)
            dx = obj['pos'][0] - cat_pos[0]
            dy = obj['pos'][1] - cat_pos[1] # Vertical height difference
            dz = obj['pos'][2] - cat_pos[2]
            
            horizontal_dist = math.sqrt(dx**2 + dz**2)
            
            # 2. Check if the object is within the feline's physical reach
            is_reachable = horizontal_dist <= self.max_jump_distance
            is_climbable = 0 < dy <= self.max_jump_height
            
            # 3. Check if the surface is wide enough to land on
            has_enough_space = obj['width'] >= self.min_surface_width

            if is_reachable and is_climbable and has_enough_space:
                print(f" > [MATCH]: {obj['label']} detected at height +{dy}m.")
                valid_ledges.append(obj)

        return valid_ledges

    def execute_jump(self, target_ledge):
        """Triggers the jump animation logic for stray_logic.py"""
        if target_ledge:
            print(f"\n[STRAY]: Performing precision jump to {target_ledge['label']}...")
            print("--- [Physics Sync]: Target coordinates locked. Transitioning state to AIRBORNE. ---")

# --- Environment Simulation Data ---
# Representing objects in the Slums (x, y, z)
urban_environment = [
    {'label': 'Rusty AC Unit', 'pos': (1.5, 2.0, 0.5), 'width': 0.8},
    {'label': 'High Neon Sign', 'pos': (2.0, 6.5, 1.0), 'width': 1.5}, # Too High
    {'label': 'Narrow Pipe', 'pos': (1.0, 1.8, -0.5), 'width': 0.15}, # Too Narrow
    {'label': 'Wooden Crate', 'pos': (0.5, 0.7, 0.0), 'width': 1.2},
]

# --- Testing the Logic ---
def run_nav_test():
    navigator = VerticalNavigator()
    my_cat_pos = (0, 0, 0) # Start on the ground

    # Scan for jumpable targets
    targets = navigator.scan_environment(my_cat_pos, urban_environment)

    if targets:
        # Automatically select the best target (e.g., the closest one)
        best_target = targets[0] 
        print(f"\n[UI Prompt]: Press [SPACE] to jump to {best_target['label']}")
        navigator.execute_jump(best_target)
    else:
        print("\n[B-12]: No valid ledges found in range.")

if __name__ == "__main__":
    run_nav_test()
