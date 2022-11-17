from gpiozero import AngularServo
from time import sleep
from app.settings import DEFAULT_ALARM_ID

SERVO_PIN = 17

# def ring_bell():
#   ring_once()

# def ring_once():
#   s = AngularServo(SERVO_PIN, initial_angle=0)
#   s.mid()
#   sleep(2)
#   s.angle = -10
#   sleep(0.1)
#   s.mid()
#   sleep(0.1)
#   s.detach()
#   sleep(5)


