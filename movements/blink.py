        
from naoqi import ALProxy
import time
from settings import IP_ADDRESS
from settings import PORT
def blink():
    leds = ALProxy("ALLeds", IP_ADDRESS, PORT)
    rDuration = 0.05
    leds.post.fadeRGB( "FaceLed0", 0x000000, rDuration )
    leds.post.fadeRGB( "FaceLed1", 0x000000, rDuration )
    leds.post.fadeRGB( "FaceLed2", 0xffffff, rDuration )
    leds.post.fadeRGB( "FaceLed3", 0x000000, rDuration )
    leds.post.fadeRGB( "FaceLed4", 0x000000, rDuration )
    leds.post.fadeRGB( "FaceLed5", 0x000000, rDuration )
    leds.post.fadeRGB( "FaceLed6", 0xffffff, rDuration )
    leds.fadeRGB( "FaceLed7", 0x000000, rDuration )
    time.sleep( 0.1 )
    leds.fadeRGB( "FaceLeds", 0xffffff, rDuration )
