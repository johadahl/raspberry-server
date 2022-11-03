import RPi.GPIO as GPIO
import time

SERVO_PIN = 17

def ring_once():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    p = GPIO.PWM(SERVO_PIN, 50)
    p.start(2.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    GPIO.cleanup()

def ring_bell():
  ring_once()