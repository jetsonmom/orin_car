# orin_car
dc_basic.py는 코드를 waveshare에서 가져와서 수정을 했다.
처음에 모터가 작동을 한 방향으로만해서 아두이노 때 h-bridge생각하고 수정을 해보았더니 잘 된다.
사실 dcmotor.py로 해야 서보조향이 자유롭게 될텐데  다시 수정을 해봐야겠다. 그리고 whisper로 다시 도전을 할텐데...
#orin, motor drive hat, pca9685로 구성
#dcmotor.py코드 실행시 에러는 안나지만 자동차가 움직이지 않는다

```
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
```
