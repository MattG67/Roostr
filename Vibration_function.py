from machine import Pin, PWM
from time import sleep

# ==============================
# PHYSICAL CONNECTIONS
# ==============================

BUZZER_PIN = 3
# Connect the positive (+) side of the buzzer to GP3.
# Connect the negative (-) side of the buzzer to GND.


# ==============================
# BUZZER SETUP
# ==============================

buzzer = PWM(Pin(BUZZER_PIN))


# ==============================
# BUZZER SETTINGS
# ==============================

HIGH_PITCH = 800      # Frequency in Hz
LOW_PITCH = 600         # Frequency in Hz

BUZZER_VOLUME = 32768   # 50% duty cycle
BUZZER_OFF = 0          # 0% duty cycle = OFF


# ==============================
# PROGRAM
# ==============================

while True:

    # HIGH-PITCH BEEP
    buzzer.freq(HIGH_PITCH)
    buzzer.duty_u16(BUZZER_VOLUME)
    sleep(0.3)


    # LOW-PITCH BEEP
    buzzer.freq(LOW_PITCH)
    sleep(0.3)


    # TURN BUZZER OFF
    buzzer.duty_u16(BUZZER_OFF)
    sleep(0.3)

