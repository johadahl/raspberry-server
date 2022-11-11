from gpiozero import AngularServo
from time import sleep

SERVO_PIN = 17

def ring(repeat=2):
    s = AngularServo(SERVO_PIN, initial_angle=0)
    
    while rung := 0 < repeat:
        s.mid()
        sleep(2)
        s.angle = -10
        sleep(0.1)
        s.mid()
        sleep(0.1)
        s.detach()
        sleep(5)
        rung += 1

def ring_bell():
  ring()