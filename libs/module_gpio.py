# #############################################################################
# ### GPIO
# ### V 1.00
# #############################################################################
from machine import Pin, I2C # type: ignore
import libs.mcp23017_raw as mcp23017
from time import sleep # type: ignore


class GPIO:

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(21), sda=Pin(20))
        self.mcp = mcp23017.MCP23017(self.i2c, 0x20)
        self.inputs = 0x00
        self.outputs = 0x00
        self.blink_store = 0x00
        self.blink_flag = False

    def get_input_byte(self):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs

    def get_input_bit(self, bit):
        self.inputs = int.from_bytes(self.mcp._read(0x13, 1), 'big')
        return self.inputs & ( 1 << bit)
    
    def get_value_bit(self, bit):
        return self.inputs & ( 1 << bit)

    def set_output_byte(self, value=None):
        if not value == None:
            self.outputs = value
        self.mcp._write([0x12, self.outputs])
        return self.outputs
    
    def set_output_bit(self, bit, value):
        if value == "On":
            self.outputs = self.outputs | ( 1 << bit)
        else:
            self.outputs = self.outputs & ~( 1 << bit)
        self.mcp._write([0x12, self.outputs])
        return self.outputs

    def all_off(self):
        self.outputs = 0x00
        self.mcp._write([0x12, self.outputs])
        return self.outputs

    def all_on(self):
        self.outputs = 0xFF
        self.mcp._write([0x12, self.outputs])
        return self.outputs

    def blink_out(self):
        if self.blink_flag == True:
            #print("Blink On")
            self.mcp._write([0x12, self.outputs])
            self.blink_flag = False
        else:
            #print("Blink Off")
            self.mcp._write([0x12, 0x00])
            self.blink_flag = True


# -----------------------------------------------------------------------------
def main():

    print("=== Start Main -> GPIO-Modul ===")

    try:
        print("Start")

        gpio = GPIO()

        gpio.set_output_bit(0, "On")
        gpio.set_output_bit(1, "On")
        gpio.set_output_bit(2, "On")
        gpio.set_output_bit(3, "On")
        gpio.set_output_bit(4, "On")
        gpio.set_output_bit(5, "On")
        gpio.set_output_bit(6, "On")
        gpio.set_output_bit(7, "On")
        gpio.set_output_bit(8, "On")
        
        sleep(1)

        gpio.set_output_bit(0, "Off")
        gpio.set_output_bit(1, "Off")
        gpio.set_output_bit(2, "Off")
        gpio.set_output_bit(3, "Off")
        gpio.set_output_bit(4, "Off")
        gpio.set_output_bit(5, "Off")
        gpio.set_output_bit(6, "Off")
        gpio.set_output_bit(7, "Off")
        gpio.set_output_bit(8, "Off")
        
        gpio.blink_out()    

        gpio.set_output_bit(0, "On")

        sleep(0.5)

        gpio.blink_out() 

        sleep(0.5)

        gpio.blink_out()

        sleep(0.5)

        gpio.blink_out()

        sleep(0.5)

        gpio.blink_out()

        sleep(0.5)


    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
    print("=== End Main ===")

# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
