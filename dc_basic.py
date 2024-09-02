#!/usr/bin/python
import smbus as smbus
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from Adafruit_GPIO import I2C
from Adafruit_PCA9685 import PCA9685  # Adafruit의 PCA9685 클래스를 사용

motor = 1
Dir = [
    'forward',
    'backward',
]

# I2C 버스 번호 7을 명시적으로 지정
pwm = PCA9685(0x40, busnum=7)  # 0x40은 기본 I2C 주소, busnum은 Jetson Nano의 I2C 버스 번호

try:
    pwm.set_pwm_freq(50)  # PWM 주파수를 50Hz로 설정
except AttributeError:
    pass  # 오류가 발생하면 무시

class MotorDriver:
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, direction, speed):
        if speed > 100:
            return
        
        duty_cycle = int(speed * 40.95)  # 0-100 범위를 0-4095로 변환

        if motor == 0:
            pwm.set_pwm(self.PWMA, 0, duty_cycle)
            if direction == Dir[0]:  # 'forward'
                pwm.set_pwm(self.AIN1, 0, 0)
                pwm.set_pwm(self.AIN2, 0, 4095)
            else:  # 'backward'
                pwm.set_pwm(self.AIN1, 0, 4095)
                pwm.set_pwm(self.AIN2, 0, 0)
        else:
            pwm.set_pwm(self.PWMB, 0, duty_cycle)
            if direction == Dir[0]:  # 'forward'
                pwm.set_pwm(self.BIN1, 0, 0)
                pwm.set_pwm(self.BIN2, 0, 4095)
            else:  # 'backward'
                pwm.set_pwm(self.BIN1, 0, 4095)
                pwm.set_pwm(self.BIN2, 0, 0)

    def MotorStop(self, motor):
        if motor == 0:
            pwm.set_pwm(self.PWMA, 0, 0)
        else:
            pwm.set_pwm(self.PWMB, 0, 0)

try:
    Motor = MotorDriver()
    # 두 모터 제어
    Motor.MotorRun(0, 'forward', 100)
    Motor.MotorRun(1, 'backward', 100)
    time.sleep(10)
    Motor.MotorRun(1, 'forward', 100)
    Motor.MotorRun(0, 'backward', 100)
    time.sleep(10)
    Motor.MotorRun(1, 'forward', 0)
    Motor.MotorRun(0, 'backward', 0)
    print("Motor is running")
    while True:
        time.sleep(1)

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("\r\nctrl + c:")
    Motor.MotorStop(0)
    Motor.MotorStop(1)
    exit()


