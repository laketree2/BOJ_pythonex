n, k = map(int, input().split()) #국가의 수 n, 등수를 알고 싶은 국가 k 입력받기
rank_list = [] #나라별 랭크 담을 리스트 생성

for _ in range(n): #국가 별 실적 계산위해 반복
    ranking = list(map(int, input().split())) #입력받기
    if ranking[0] != k: #k나라보다 잘하는 나라가 몇 개인가를 위해 k제외
        rank_list.append(ranking) #랭크 저장
    else: #k나라일 경우
        country_k = ranking #k나라 랭크 저장

count = 1 #등수 = 자신보다 더 잘한 나라 수 +1를 위해 1설정
for i in range(len(rank_list)): #반복
    if rank_list[i][1] > country_k[1]: #k나라보다 금메달이 많을 경우
        count += 1 #무조건 등수가 높으므로 추가

    elif rank_list[i][1] == country_k[1]: #금메달의 개수가 같으면
        if rank_list[i][2] > country_k[2]: #은메달의 개수를 비교해 많으면
            count += 1 #추가

        elif rank_list[i][2] == country_k[2]: #은메달까지 같으면
            if rank_list[i][3] > country_k[3]: #동메달 개수를 비교하고 많으면
                count += 1 #추가
#금메달 은메달 동메달 개수가 똑같거나 k나라보다 성적이 떨어지는 나라는 고려 대상에서 제외

print(count) #출력