###설문
#성향테스트

import sys
score = 0
answer_one = 0
answer_two = 0
answer_three = 0
answer_four = 0
answer_five = 0
answer_six = 0 
answer_seven = 0
answer_eight = 0

answer_one = int(input("""1 당신의 연령대는 어떻게 됩니까?
1. 19세 이하
2. 20세~40세
3. 41세~50세
4. 51세~60세
5. 61세 이상"""))

if answer_one == 1:
    score += 12.5
elif answer_one  == 2:
    score += 12.5
elif answer_one == 3:
    score += 9.3
elif answer_one == 4:
    score += 6.2
elif answer_one == 5:
    score += 3.1
else:
    print('잘못누르셨습니다')
    sys.exit()

answer_two = int(input("""2 투자하고자 하는 자금의 투자 가능 기간은 얼마나 됩니까?
1. 6개월 이내
2. 6개월 이상~1년 이내
3. 1년 이상~2년 이내
4. 2년 이상~3년 이내
5. 3년 이상"""))

if answer_two == 1:
    score += 3.1
elif answer_two  == 2:
    score += 6.2
elif answer_two == 3:
    score += 9.3
elif answer_two == 4:
    score += 12.5
elif answer_two == 5:
    score += 15.6
else:
    print('잘못누르셨습니다')
    sys.exit()
    
answer_three = int(input("""3 다음 중 투자경험과 가장 가까운 것은 어느 것입니까?
1. 은행의 예·적금, 국채, 지방채, 보증채, MMF, CMA 등
2. 금융채, 신용도가 높은 회사채, 채권형펀드, 원금보존추구형ELS 등
3. 신용도 중간 등급의 회사채, 원금의 일부만 보장되는 ELS, 혼합형펀드 등
4. 신용도가 낮은 회사채, 주식, 원금이 보장되지 않는 ELS, 시장수익률 수준의 수익을 추구하는 주식형펀드 등
5. ELW, 선물옵션, 시장수익률 이상의 수익을 추구하는 주식형펀드, 파생상품에 투자하는 펀드, 주식 신용거래 등"""))

if answer_three == 1:
    score += 3.1
elif answer_three  == 2:
    score += 6.2
elif answer_three == 3:
    score += 9.3
elif answer_three == 4:
    score += 12.5
elif answer_three == 5:
    score += 15.6
else:
    print('잘못누르셨습니다')
    sys.exit()
    
answer_four = int(input("""4 금융상품 투자에 대한 본인의 지식수준은 어느 정도라고 생각하십니까?
1. ［매우 낮은 수준］투자의사 결정을 스스로 내려본 경험이 없는 정도
2. ［낮은 수준］주식과 채권의 차이를 구별할 수 있는 정도
3. ［높은 수준］투자할 수 있는 대부분의 금융상품의 차이를 구별할수 있는 정도
4. ［매우 높은 수준］금융상품을 비롯하여 모든 투자대상 상품의 차이를 이해할 수 있는 정도"""))

if answer_four == 1:
    score += 3.1
elif answer_four  == 2:
    score += 6.2
elif answer_four == 3:
    score += 9.3
elif answer_four == 4:
    score += 12.5
else:
    print('잘못누르셨습니다')
    sys.exit()
    
answer_five = int(input("""5 현재 투자하고자 하는 자금은 전체 금융자산(부동산 등을 제외) 중 어느 정도의 비중을 차지합니까?
1. 10% 이내
2. 10% 이상~20% 이내
3. 20% 이상~30% 이내
4. 30% 이상~40% 이내
5. 40%이상"""))

if answer_five == 1:
    score += 15.6
elif answer_five  == 2:
    score += 12.5
elif answer_five == 3:
    score += 9.3
elif answer_five == 4:
    score += 6.2
elif answer_five == 5:
    score += 3.1
else:
    print('잘못누르셨습니다')
    sys.exit()
    
answer_six = int(input ("""6 다음 중 당신의 수입원을 가장 잘 나타내고 있는 것은 어느 것입니까?
1. 현재 일정한 수입이 발생하고 있으며, 향후 현재 수준을 유지하거나 증가할 것으로 예상된다.
2. 현재 일정한 수입이 발생하고 있으나, 향후 감소하거나 불안정할 것으로 예상된다.
3. 현재 일정한 수입이 없으며, 연금이 주수입원이다."""))

if answer_six == 1:
    score += 9.3
elif answer_six  == 2:
    score += 6.2
elif answer_six == 3:
    score += 3.1
else:
    print('잘못누르셨습니다')
    sys.exit()

answer_seven = int(input("""7 만약 투자원금에 손실이 발생할 경우 다음 중 감수할 수 있는 손실 수준은 어느 것입니까?
1. 무슨 일이 있어도 투자원금은 보전되어야 한다.
2. 10% 미만까지는 손실을 감수할 수 있을 것 같다.
3. 20% 미만까지는 손실을 감수할 수 있을 것 같다.
4. 기대수익이 높다면 위험이 높아도 상관하지 않겠다."""))

if answer_seven == 1:
    score -= 6.2
elif answer_seven  == 2:
    score += 6.2
elif answer_seven == 3:
    score += 12.5
elif answer_seven == 4:
    score += 18.7
else:
    print('잘못누르셨습니다')
    sys.exit()

answer_eight = int(input("""8 퇴직연금은 세액공제 측면에서, 연금저축은 투자금 운용 측면에서 상대적 강점이 있습니다. 당신은 세액공제 혜택과 투자금의 운용성 중 무엇이 더 중요하다고 생각하십니까?
1. 퇴직연금(세액공제 한도 700만원, 적립금의 70%까지 주식형 펀드·상장지수펀드(ETF) 투자 가능)
2. 연금저축(세액공제 한도 400만원, 적립금의 100%까지 주식형 펀드·상장지수펀드(ETF) 투자 가능)"""))

if answer_eight == 1:
    category = '퇴직연금'
elif answer_eight == 2:
    category = '연금저축'
else:
    print('잘못누르셨습니다')
    sys.exit()
        

if score <= 20:
    tendency = "안정형"
elif score <= 40:
    tendency = "안정추구형"
elif score <= 60:
    tendency = "위험중립형"
elif score <= 80:
    tendency = "적극투자형"
else:
    tendency = "공격투자형"
        
print(f"""=====성향분석결과=====
1. 안정형 20점 이하
2. 안정추구형 20점 초과~40점 이하
3. 위험중립형 40점 초과~60점 이하
4. 적극투자형 60점 초과~80점 이하
5. 공격투자형 80점 초과
당신의 점수는 {round(score,2)}점으로, {tendency}입니다.
당신의 성향에 맞는 {category}상품을 추천해드리겠습니다.""")