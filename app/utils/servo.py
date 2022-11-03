from gpiozero import AngularServo
from time import sleep

SERVO_PIN = 17

def ring_once():
    s = AngularServo(17, initial_angle=0)
    while True:
        sleep(2)
        s.angle = -10
        sleep(0.1)
        s.mid()
        sleep(0.1)
        s.detach()
        sleep(5)

def ring_bell():
  ring_once()