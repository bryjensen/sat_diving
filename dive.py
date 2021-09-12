# What or is there going to be a base code to make all the code functions
# Start with a class, all the equipment can basically be the same

# make a function up here than store it and apply it as needed.
# make a bunch at random first than start putting them together

# Some signal that transfers through, how much do other, default for the program is to keep equipment on
# Will monitor what the computer is doing but the computer cannot do anything unless an input has been sent by the tech.


# global alarm = a signal with self_identifier on one field, one alarm circuit 



class reclaim:
    # Power should be first for everything
    def power[Stby, Off, On]:
        if On == 1:
            return red 
        elif Off == 0:
            return green
        # Just use mod number to identify problem, so
        elif Stby == {num}
        else:
            return amber
    # What do you need to use for a loop, the working_pressure, O2_injection, HeO2_injection, magnetic_switch, electricity(signal, power for what), air_pressure or 
    # motor_driven. Balancing the pyramids, how to keep the balance
    def maintain_volume(maintain, high, low):
        if maintain < low:    # maintain is the high and low, so notes    
            HeO2_injection == True    # True: The pressure is to low. False: The pressure is not to low(high pressure is reached)

class environmental_control_unit:
    def hot_supply(temperature, high, low): # True: Temp is to low. False: The temp is not to low(high temperature is reached)
        if temperature == low:
            return alarm[True]
            # temperatur sensor
        elif temperature == high:
            return alarm[False]
            # temperature sensor
        # input() to set low and high        
        # range to be an input that is changed from an external source, ie dive sup, tech, lst. Maybe use a global function to define the input, who has input to what
    
    def supply_water(pressure, volume, loops): # how many loops do you need for what to operate, a gravity effect, the average is nothing, lowest energy state.
        bool[pressure > alarm_level[supply_water]] 
        bool[volume > alarm_level[supply_volume]]
        # pressure switch that is electrical
        # which level do you need to make loops for cross-dimensional communication
        # what are root functions for what, independent monitors
    
    def heating_tank_element([signal, False, True]):
        if signal == True:
            return True
        # normally open switch that closes to send power when needed
    

    def cold_supply(temperature, high, low): # True: Temp is to low. False: The temp is not to low(high temperature is reached)
        if temperature == low:
            return alarm[True]
        elif temperature == high:
            return alarm[False]
    
    def compressor






class alarms:
    # storage for the original code take this code to where it is needed
    # code for the AI to follow, go to readme
    # need global commands for cross class communications
    def CO2_alarm_DDC(sensor, high, low):
        CO2.readout.chamber_DDC()
        print(f"{sensor}, {high}, {low}")
        # need commands for high and low, what does high do, what does low do, normally open, normally close. turn off, turn on, superposition and uncertainty level of how long what takes to make which change.

    def O2_alarm_DDC(sensor, high, low):
        O2.readout.chamber_DDC()
        print(f"{sensor}, {high}, {low}")

    def He_alarm_DDC(input(sensor), high, low):
        He.readout.chamber_DDC()
        print(f"{input(sensor)}, {high}, {low}")
    
    def random_alarm_DDC(input(sensor), high, low):
        random.readout.chamber_DDC()
        print(f"{input(sensor)}, {high}, {low}")

    def depth_alarm_DDC(input(sensor), high, low):
        depth.readout.chamber_DDC()
        print(f"{input(sensor)}, {high}, {low}")

    # global commands allowed by who. lst, tech, superintendent, where does what decision making go. who gets control over what or who overrides who. everyone has access to see what is happening but only {position} gets to change what part of what. a computerized log with a messenger attached to make statements.



class lars:
    # using magnetic and pressure (laser or what makes a double switch redundancy) switches with a dual redundancy to proceed to next step
    # bell coming up pushes or lifts a weight(can't think of better word)
    def hydraulics[Stby, Off, On]: # Amber can be on with either red or green but red and green cannot be on at the same time
        def power[Stby, Off, On]:
            if On == 1:
                return red
            elif Off == 0:
                return green
            else:
                return amber

        def where_the_power_goes[{internal_computer}, {motor}, {'?'}]:
            if On:
                return red
            elif Off:
                return green
            else:
                return amber

        def alarm[pressure_sensor_where, alarm_high, alarm_low]:
            if On:
                return red # because it is on red is hot
            elif Off:
                return green
            else:
                return amber
            # sensors for display of amber, the ai_interface has troubleshooting installed, return code to identify problem, can ai_ or computer fix itself or does it need external.
            # maybe something else
            # if alarm_high == 1:
            #     return red 
            # elif alarm_low == 0:
            #     return green
            # else:
            #     return amber






class equipment:
    def power = [Stby, Off, On]: # Boolean, False = Off and True = On . Superposition of Stby points to what, red, green, amber, how are what lights on
        def power[On] = circuit.closed:
            def monitor_power = range(AC/DC)


