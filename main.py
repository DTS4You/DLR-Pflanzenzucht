######################################################
### Main-Program                                   ###
### Projekt: Pflanzenzucht                         ###
### Version: 1.00                                  ###
### Datum  : 14.04.2026                            ###
######################################################
from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore

LOOP_DELAY      = 0.05          # typ. 50 ms

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Start Main ===")
    
    on_state        = False

    gpio = MyGPIO.GPIO()

    print("Setup Default")

    MyWS2812.do_all_off()	# Alle Leds auf "AUS"
    gpio.all_off()
    
    time.sleep(0.3)

    print(">>> Main-Loop >>>")

    try:       
        # Loop forever !!!
        while True:
            if gpio.get_input_bit(0):
                time.sleep(0.05)
                print("Taster gedrückt")
                if on_state == False:
                    MyWS2812.do_all_on()
                    gpio.set_output_byte(0xFF)
                    on_state = True
                else:
                    MyWS2812.do_all_off()
                    gpio.set_output_byte(0x00)
                    on_state = False
                time.sleep(0.5)
            # Loop-Delay !!!
            time.sleep(LOOP_DELAY)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")
        MyWS2812.do_all_off()
        gpio.set_output_byte(0x00)

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_gpio:
        print("I2C_GPIO -> Load-Module")
        import libs.module_gpio as MyGPIO
    else:
        print("I2C_GPIO -> nicht vorhanden")

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___ -> = STOP =")

# ##############################################################################
