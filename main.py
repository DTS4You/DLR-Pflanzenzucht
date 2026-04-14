######################################################
### Main-Program                                   ###
### Projekt: Bereich-Raumfahrt                     ###
### Version: 1.00                                  ###
### Datum  : 08.12.2025                            ###
######################################################
from machine import Pin, Timer                              # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore

LOOP_DELAY      = 0.01          # typ. 10 ms

map_array_01 = [ 1]
map_array_02 = [ 2]
map_array_03 = [ 3]
map_array_06 = [ 4]
map_array_04 = [ 5]
map_array_05 = [ 6]
map_array_07 = [ 7]
map_array_08 = [ 8]
map_array_09 = [ 9]
map_array_10 = [10]
map_array_11 = [11]
map_array_12 = [12]
map_array_13 = [13]
map_array_14 = [14]
map_array_15 = [15]
map_array_16 = [16]


obj_offset = 0          # Offset bei Zählung ab 1 = -1

def blink_func():
    MyWS2812.do_blink()


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Start Main ===")
    
    blink_couter = 0

    gpio = MyGPIO.GPIO()

    try:
        
        print("Start Main Loop")
 
        for i in range(3):
            gpio.set_output_bit(0, "On")
            gpio.set_output_bit(1, "On")
            gpio.set_output_bit(2, "On")
            gpio.set_output_bit(3, "On")
            gpio.set_output_bit(4, "On")
            gpio.set_output_bit(5, "On")
            gpio.set_output_bit(6, "On")
            gpio.set_output_bit(7, "On")
            time.sleep(0.3)
            gpio.set_output_bit(0, "Off")
            gpio.set_output_bit(1, "Off")
            gpio.set_output_bit(2, "Off")
            gpio.set_output_bit(3, "Off")
            gpio.set_output_bit(4, "Off")
            gpio.set_output_bit(5, "Off")
            gpio.set_output_bit(6, "Off")
            gpio.set_output_bit(7, "Off")
            time.sleep(0.3)

        print("GPIO Test Ende")

        MyWS2812.do_all_def()	# Alle Leds auf Default-Wert
        gpio.all_off()
       
        # True
        while MySerial.sercon_read_flag():

            if blink_couter > 50:
                blink_couter = 0
                blink_func()
                gpio.blink_out()
        
            MySerial.sercon_read_line()
            if MySerial.get_ready_flag():       # Zeichenkette empfangen
                print(MySerial.get_string())
                MyDecode.decode_input(str(MySerial.get_string()))
                #MyDecode.decode_printout()
                if MyDecode.get_valid_flag() == True:
                    #print("Valid Command")
                    if MyDecode.get_cmd_1() == "do":
                        #print("do")
                        if MyDecode.get_cmd_2() == "all":
                            #print("all")
                            if MyDecode.get_value_1() == 0:
                                #print("off")
                                MyWS2812.do_all_off()
                                gpio.all_off()
                            if MyDecode.get_value_1() == 1:
                                #print("on")
                                MyWS2812.do_all_on()
                                gpio.all_on()
                            if MyDecode.get_value_1() == 2:
                                #print("def")
                                MyWS2812.do_all_def()
                                #gpio.set_output_byte(0x00)
                                gpio.all_off()

                        if MyDecode.get_cmd_2() == "obj":
                            #print("obj")
                            #print(MyDecode.get_value_1())
                            #print(segment_map[MyDecode.get_value_1()])
                            MyWS2812.do_all_off()
                            #gpio.set_output_byte(0x00)
                            #==> Function -01-
                            if MyDecode.get_value_1() == 1:
                                for i in map_array_01:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(5, "On")
                                    #pass
                            #==> Function -02-
                            if MyDecode.get_value_1() == 2:
                                for i in map_array_02:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(2, "On")
                                    #pass
                            #==> Function -03-
                            if MyDecode.get_value_1() == 3:
                                for i in map_array_03:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(4, "On")
                                    #pass
                            #==> Function -04-
                            if MyDecode.get_value_1() == 4:
                                for i in map_array_04:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(1, "On")
                                    pass
                            #==> Function -05-
                            if MyDecode.get_value_1() == 5:
                                for i in map_array_05:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(3, "On")
                                    #pass
                            #==> Function -06-
                            if MyDecode.get_value_1() == 6:
                                for i in map_array_06:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    gpio.all_off()
                                    gpio.set_output_bit(0, "On")
                                    #pass
                            #==> Function -07-
                            if MyDecode.get_value_1() == 7:
                                for i in map_array_07:
                                    MyWS2812.set_led_obj(2, MyDecode.get_value_2())
                                    gpio.all_off()
                                    #gpio.set_output_byte(0x00)
                            #==> Function -08-
                            if MyDecode.get_value_1() == 8:
                                for i in map_array_08:
                                    MyWS2812.set_led_obj(4, MyDecode.get_value_2())
                                    gpio.all_off()
                                    #gpio.set_output_byte(0x00)
                            #==> Function -09-
                            if MyDecode.get_value_1() == 9:
                                for i in map_array_09:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    #gpio.set_output_byte(0x00)
                                    pass
                            #==> Function -10-
                            if MyDecode.get_value_1() == 10:
                                for i in map_array_10:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    #gpio.set_output_byte(0x00)
                                    pass
                             #==> Function -11-
                            if MyDecode.get_value_1() == 11:
                                for i in map_array_11:
                                    MyWS2812.set_led_obj(1, MyDecode.get_value_2())
                                    gpio.all_off()
                                    #gpio.set_output_byte(0x00)
                                    pass
                            #==> Function -51-
                            if MyDecode.get_value_1() == 51:
                                for i in map_array_11:
                                    MyWS2812.set_led_obj(3, MyDecode.get_value_2())
                                    #time.sleep(0.1)
                                    #gpio.set_output_byte(0x00)
                            #==> Function -52-
                            if MyDecode.get_value_1() == 52:
                                for i in map_array_12:
                                    MyWS2812.set_led_obj(0, MyDecode.get_value_2())
                                    #time.sleep(0.1)
                                    #gpio.set_output_byte(0x00)
                            #==> Function -13-
                            if MyDecode.get_value_1() == 13:
                                for i in map_array_13:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass
                            #==> Function -14-
                            if MyDecode.get_value_1() == 14:
                                for i in map_array_14:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass
                            if MyDecode.get_value_1() == 15:
                                for i in map_array_15:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass
                            if MyDecode.get_value_1() == 16:
                                for i in map_array_16:
                                    #MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                                    pass

                            #MyWS2812.set_led_obj(MyDecode.get_value_1(), MyDecode.get_value_2())


            blink_couter = blink_couter + 1
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
