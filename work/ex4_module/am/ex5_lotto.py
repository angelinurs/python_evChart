import random;

# 절대 중복이 안되는 자료구조
lotto = set();

# 위의 set구조가 총 6개가 될 때까지 무한 반복을 해야 한다.
while True:
    value = random.choice(range(1,46));# 1~45까지의 수들 중 난수 발생
    lotto.add(value);
    if len(lotto) == 6: # lotto에 저장된 수가 6일 때 반복문 탈출
        break;

print("lotto:", lotto);    
