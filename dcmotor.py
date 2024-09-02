from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from Adafruit_GPIO.I2C as I2C
I2C.require_repeater_start()
import time
#I2C.busnum = 7
 모터햇 설정
mh = Adafruit_MotorHAT(addr=0x40)  # 기본 I2C 주소는 0x60입니다.

# DC 모터 초기화
motor = mh.getMotor(1)  # M1, M2, M3, M4 중 하나를 선택

# 모터 정지 함수
def stop_motor():
    motor.run(Adafruit_MotorHAT.RELEASE)

# 프로그램 종료 시 모든 모터 정지
import atexit
atexit.register(stop_motor)

class VehicleController:
    def __init__(self):
        self.k_throttle = 255  # 모터 속도 (0-255)

    def perform_sequence(self):
        # 앞으로 이동
        motor.setSpeed(self.k_throttle)
        motor.run(Adafruit_MotorHAT.FORWARD)
        time.sleep(3)

        # 뒤로 이동
        motor.setSpeed(self.k_throttle)
        motor.run(Adafruit_MotorHAT.BACKWARD)
        time.sleep(3)

        # 모터 정지
        motor.run(Adafruit_MotorHAT.RELEASE)
        time.sleep(1)

if __name__ == "__main__":
    controller = VehicleController()
    controller.perform_sequence()



