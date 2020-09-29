import json

'''
toddler
kinder
elem
middle
high
parents : 부모 부양 여부 모시고 있으면 1 아니면 0
p3~p10중에 pn - p1이 > 18인 개수
child : 초등학생 이하 자녀 존재 여부
teenager : 중, 고등학생 자녀 존재 여부
age_c : 연령대
'''


def calc_parent(lis):
    cnt = 0
    p1_age = lis[0]
    for n in lis[1:]:   # p1, p2를 뺀다
       if n != None and n - p1_age > 19:
           cnt += 1
    return 1 if cnt > 0 else 0

def calc_info(lis, fr ,to):
    cnt = 0
    for n in lis[1:]:   # p1을 뺀다
        if n != None and fr <= n < to:
            cnt += 1
    return cnt

def calc_age_c(age):
    '''
    # age_c 는
    1: 0~29
    2: 30~39
    3: 40~49
    4: 50~59
    5: 60~69
    6: 70~79
    7: 그 이상
    '''

    if age <= 29:
       return 1
    elif age >= 80:
        return 7
    else:
        return age // 10 + 1
