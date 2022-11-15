'''
Window 판다스 설치
  pip install pandas
  
Mac 판다스 설치
  python3 -m pip install pandas
  
Pandas는 데이터를 수정하고 목적에 맞도록 가공이 가능하도록
제공되는 라이브러리이며, 내부적으로 NumPy를 사용하고 있어서
숫자 데이터들의 연산이 상당히 원활하다.

의미 있는 정보를 추출하는 기술은 최근 들어 매우 주목 받고 있다.

최근들어 분석할 데이터의 양(Volume)이 커지고,
데이터의 입출력 속도(Velocity)가 빨라지고,
데이터의 종류가 다양해(Variety) 지면서 데이터 분석 분야의 주목을 받게 되었다.

Volume, Velocity, Variety의 세 가지 'V'를 가진 데이터를 흔히
'빅 데이터'라고 부른다.

이런 빅데이터들을 분석하는 것이 Pandas다. 그리고 Pandas를 이해하려면
DataFrame을 이해해야 한다.

즉, DataFrame이란 것은 DB로 비유하면 테이블과 같은 의미다.
그러면 테이블은 컬럼들이 있다. 이런 컬럼에 속하는 것이 Pandas에서는
Series라고 한다.
'''
import pandas as pd;

ko = pd.Series([96200, 89700, 94300, 99000]);
print(ko);





