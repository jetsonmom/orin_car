# orin_car
orin, motor drive hat, pca9685로 구성
dcmotor.py코드 실행시 에러
***
orin@orin-desktop:~$ python3 dcmotor.py
Traceback (most recent call last):
  File "/home/orin/dcmotor.py", line 4, in <module>
    mh = Adafruit_MotorHAT(addr=0x40)  # 기본 I2C 주소는 0x60입니다.
  File "/home/orin/.local/lib/python3.10/site-packages/Adafruit_MotorHAT/Adafruit_MotorHAT_Motors.py", line 231, in __init__
    self._pwm = PWM(addr, debug=False, i2c=i2c, i2c_bus=i2c_bus)
  File "/home/orin/.local/lib/python3.10/site-packages/Adafruit_MotorHAT/Adafruit_PWM_Servo_Driver.py", line 57, in __init__
    self.i2c = get_i2c_device(address, i2c, i2c_bus)
  File "/home/orin/.local/lib/python3.10/site-packages/Adafruit_MotorHAT/Adafruit_PWM_Servo_Driver.py", line 21, in get_i2c_device
    return I2C.get_i2c_device(address)
  File "/home/orin/.local/lib/python3.10/site-packages/Adafruit_GPIO/I2C.py", line 63, in get_i2c_device
    busnum = get_default_bus()
  File "/home/orin/.local/lib/python3.10/site-packages/Adafruit_GPIO/I2C.py", line 55, in get_default_bus
    raise RuntimeError('Could not determine default I2C bus for platform.')
RuntimeError: Could not determine default I2C bus for platform.
***
orin@orin-desktop:~$ i2cdetect -y -r 7
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                      
