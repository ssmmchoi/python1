from statistics import mean  # 통계함수
from math import sqrt  # 수학함수

# 평균함수
def Avg(dataset) :
    return mean(dataset)

# 분산과 표준편차 함수

def var_std(dataset) :
    avg = Avg(dataset)  # 산술평균
    # avg = mean(dataset) # auch 산술평균

    # list + for
    diff = [(x-avg)**2 for x in dataset]  # (x변량-평균)**2
    diff_sum = sum(diff)

    var = diff_sum / (len(dataset) - 1) # 분산
    std = sqrt(var) # 표준편차
    return var, std

datas = [2,3,5,6,7,8.5]
print(Avg(datas))
