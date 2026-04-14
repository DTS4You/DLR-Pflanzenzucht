# #############################################################################
# ### MyGlobal
# ### Bereich Raumfahrt V1.00
# #############################################################################

class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True
    inc_gpio            = True


class Global_WS2812:

    numpix_1            = 64            # Anzahl LEDs im 1. Stripe
    numpix_2            = 64            # Anzahl LEDs im 2. Stripe
    numpix_3            = 64            # Anzahl LEDs im 3. Stripe
    numpix_4            = 64            # Anzahl LEDs im 4. Stripe
    numpix_5            = 64            # Anzahl LEDs im 5. Stripe
    numpix_6            = 64            # Anzahl LEDs im 6. Stripe
    numpix_7            = 64            # Anzahl LEDs im 7. Stripe
    numpix_8            = 64            # Anzahl LEDs im 8. Stripe

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe      # 1. LED-Stripe
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = 63            #  1. Ledsegment -> Anzahl

    seg_02_strip        = 1             #  2. Ledsegment -> Stripe      # 2. LED-Stripe
    seg_02_start        = 0             #  2. Ledsegment -> Start
    seg_02_count        = 63            #  2. Ledsegment -> Anzahl

    seg_03_strip        = 2             #  3. Ledsegment -> Stripe      # 3. LED-Stripe
    seg_03_start        = 0             #  3. Ledsegment -> Start
    seg_03_count        = 63            #  3. Ledsegment -> Anzahl
    
    seg_04_strip        = 3             #  4. Ledsegment -> Stripe      # 4. LED-Stripe
    seg_04_start        = 0             #  4. Ledsegment -> Start
    seg_04_count        = 63            #  4. Ledsegment -> Anzahl

    seg_05_strip        = 4             #  5. Ledsegment -> Stripe      # 5. LED-Stripe
    seg_05_start        = 0             #  5. Ledsegment -> Start
    seg_05_count        = 63            #  5. Ledsegment -> Anzahl
    
    seg_06_strip        = 5             #  6. Ledsegment -> Stripe      # 6. LED-Stripe
    seg_06_start        = 0             #  6. Ledsegment -> Start
    seg_06_count        = 63            #  6. Ledsegment -> Anzahl
    
    seg_07_strip        = 6             #  7. Ledsegment -> Stripe      # 7. LED-Stripe
    seg_07_start        = 0             #  7. Ledsegment -> Start
    seg_07_count        = 63            #  7. Ledsegment -> Anzahl

    seg_08_strip        = 7             #  8. Ledsegment -> Stripe      # 8. LED-Stripe
    seg_08_start        = 0             #  8. Ledsegment -> Start
    seg_08_count        = 63            #  8. Ledsegment -> Anzahl
    
# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  5)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_half          = ( 50, 50, 50)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (  0,200,  0)
    color_blink_off     = (  0, 10,  0)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()