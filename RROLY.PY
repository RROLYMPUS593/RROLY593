import time

class Olympus593:
    # Constants
    TAKEOFF_SPEED = 455
    SUBSONIC_SPEED = 1234
    SUPERSONIC_SPEED = 2436

    def __init__(self, engine_id):
        # Engine parameters
        self.engine_id = engine_id
        self.throttle_position = 0
        self.rpm = 0
        self.temperature = 0
        self.reheat = False
        self.operating_time = 0  # in hours

        # Component lifetimes
        self.compressor_blades_lifetime = 10000  # in hours
        self.turbine_blades_lifetime = 10000  # in hours
        self.engine_lifetime = 25000  # in hours

        # Intake parameters
        self.intake_pressure_ratio = 1.0
        self.boundary_layer_removed = False
        self.dump_doors_open = False
        self.auxiliary_inlet_open = False
        self.intake_position = 0  # Intake geometry position (0-100%)

        # Exhaust nozzle parameters
        self.exhaust_nozzle_position = 0  # Exhaust nozzle position (0-100%)
        self.eyelids_closed = False

        # Component lifetimes
        self.primary_nozzle_lifetime = 30000  # in hours
        self.thrust_reverser_lifetime = 40000  # in hours

        # Engine size and performance characteristics
        self.length = 4.039  # in meters
        self.diameter = 1.212  # in meters
        self.dry_weight = 3175  # in kg

        # Performance characteristics
        self.max_thrust_wet = 169200  # in Newtons
        self.max_thrust_dry = 139400  # in Newtons
        self.overall_pressure_ratio_stationary = 15.5
        self.air_mass_flow = 186  # in kg/s
        self.specific_fuel_consumption_cruise = 1.195  # in lb/(lbf⋅h)
        self.thrust_to_weight_ratio = 5.4

        # Additional parameters for simulation
        self.airspeed = 0

    def start(self):
        print(f"Olympus 593 engine {self.engine_id} starting...")
        time.sleep(2)
        print(f"Olympus 593 engine {self.engine_id} started!")

    def stop(self):
        print(f"Olympus 593 engine {self.engine_id} shutting down...")
        time.sleep(2)
        print(f"Olympus 593 engine {self.engine_id} shut down.")

    def set_throttle(self, position):
        if 0 <= position <= 100:
            self.throttle_position = position
            print(f"Engine {self.engine_id} Throttle set to {position}%")
        else:
            print(f"Error: Throttle position for Engine {self.engine_id} should be between 0 and 100.")

    def toggle_reheat(self):
        if self.throttle_position > 80:
            self.reheat = not self.reheat
            print(f"Engine {self.engine_id} Reheat {'On' if self.reheat else 'Off'}")
        else:
            print(f"Error: Reheat for Engine {self.engine_id} can only be activated above 80% throttle.")

    def toggle_eyelids(self):
        self.eyelids_closed = not self.eyelids_closed
        print(f"Engine {self.engine_id} Exhaust nozzle eyelids {'Closed' if self.eyelids_closed else 'Open'}")

    def toggle_intake_dump_doors(self):
        self.dump_doors_open = not self.dump_doors_open
        print(f"Engine {self.engine_id} Intake dump doors {'Open' if self.dump_doors_open else 'Closed'}")

    def toggle_auxiliary_inlet(self):
        self.auxiliary_inlet_open = not self.auxiliary_inlet_open
        print(f"Engine {self.engine_id} Auxiliary inlet {'Open' if self.auxiliary_inlet_open else 'Closed'}")

    def set_intake_position(self, position):
        if 0 <= position <= 100:
            self.intake_position = position
            print(f"Engine {self.engine_id} Intake position set to {position}%")
        else:
            print(f"Error: Intake position for Engine {self.engine_id} should be between 0 and 100.")

    def set_exhaust_nozzle_position(self, position):
        if 0 <= position <= 100:
            self.exhaust_nozzle_position = position
            print(f"Engine {self.engine_id} Exhaust nozzle position set to {position}%")
        else:
            print(f"Error: Exhaust nozzle position for Engine {self.engine_id} should be between 0 and 100.")

    def set_airspeed(self, airspeed):
        self.airspeed = airspeed
        print(f"Engine {self.engine_id} Airspeed set to {airspeed} km/h")

    def adjust_doors(self):
        # Adjust doors based on airspeed
        if 0 <= self.airspeed <= self.TAKEOFF_SPEED:
            self.door1_position = 1  # Takeoff or landing
            self.door2_position = 1  # Takeoff
            self.door3_position = 1  # Takeoff
        elif self.TAKEOFF_SPEED < self.airspeed <= self.SUBSONIC_SPEED:
            self.door1_position = 2  # Subsonic
            self.door2_position = 2  # Subsonic
            self.door3_position = 1  # Takeoff
        elif self.SUBSONIC_SPEED < self.airspeed <= self.SUPERSONIC_SPEED:
            self.door1_position = 3  # Supersonic
            self.door2_position = 3  # Supersonic
            self.door3_position = 1  # Takeoff

    def update(self, time_elapsed):
        # Simulate engine dynamics
        self.rpm = 1000 + 10 * self.throttle_position
        self.temperature = 150 + 0.2 * self.rpm

        # Update component lifetimes
        self.compressor_blades_lifetime -= time_elapsed
        self.turbine_blades_lifetime -= time_elapsed
        self.engine_lifetime -= time_elapsed

    def update_intake(self, time_elapsed):
        # Simulate intake adjustments
        if self.intake_position > 60 and not self.boundary_layer_removed:
            print(f"Engine {self.engine_id} Boundary layer removed.")
            self.boundary_layer_removed = True

    def update_exhaust_nozzle(self, time_elapsed):
        # Simulate exhaust nozzle dynamics
        if self.throttle_position > 80 and not self.eyelids_closed:
            self.toggle_eyelids()

    def display_status(self):
        print(f"Engine {self.engine_id} RPM: {self.rpm}")
        print(f"Engine {self.engine_id} Temperature: {self.temperature} C")

    def display_intake_status(self):
        print(f"Engine {self.engine_id} Intake Pressure Ratio: {self.intake_pressure_ratio}")
        print(f"Engine {self.engine_id} Boundary Layer Removed: {'Yes' if self.boundary_layer_removed else 'No'}")
        print(f"Engine {self.engine_id} Dump Doors: {'Open' if self.dump_doors_open else 'Closed'}")
        print(f"Engine {self.engine_id} Auxiliary Inlet: {'Open' if self.auxiliary_inlet_open else 'Closed'}")

    def display_exhaust_nozzle_status(self):
        print(f"Engine {self.engine_id} Exhaust Nozzle Position: {self.exhaust_nozzle_position}%")
        print(f"Engine {self.engine_id} Exhaust Nozzle Eyelids: {'Closed' if self.eyelids_closed else 'Open'}")

    def display_engine_specs(self):
        print(f"Engine {self.engine_id} Length: {self.length} meters")
        print(f"Engine {self.engine_id} Diameter: {self.diameter} meters")
        print(f"Engine {self.engine_id} Dry Weight: {self.dry_weight} kg")
        print(f"Engine {self.engine_id} Max Thrust (Wet): {self.max_thrust_wet} N")
        print(f"Engine {self.engine_id} Max Thrust (Dry): {self.max_thrust_dry} N")
        print(f"Engine {self.engine_id} Overall Pressure Ratio (Stationary): {self.overall_pressure_ratio_stationary}")
        print(f"Engine {self.engine_id} Air Mass Flow: {self.air_mass_flow} kg/s")
        print(f"Engine {self.engine_id} Specific Fuel Consumption (Cruise): {self.specific_fuel_consumption_cruise} lb/(lbf⋅h)")
        print(f"Engine {self.engine_id} Thrust-to-Weight Ratio: {self.thrust_to_weight_ratio}")


# Create four engines
engines = [Olympus593(engine_id=i) for i in range(1, 5)]

# Example usage
for engine in engines:
    engine.start()

try:
    for throttle in range(5):
        for engine in engines:
            engine.set_throttle(throttle * 25)  # Throttle positions: 0, 25, 50, 75, 100
            engine.set_airspeed(400)  # Set airspeed for intake adjustments
            engine.adjust_doors()
            engine.update(1)  # Time elapsed is set to 1 for simplicity, it can be adjusted as needed
            engine.update_intake(1)  # New method to simulate intake adjustments
            engine.update_exhaust_nozzle(1)  # New method to simulate exhaust nozzle adjustments
            engine.display_status()
            engine.display_intake_status()  # New method to display intake status
            engine.display_exhaust_nozzle_status()  # New method to display exhaust nozzle status
            engine.display_engine_specs()  # New method to display engine specifications
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    for engine in engines:
        engine.stop()
