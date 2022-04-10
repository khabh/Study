# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

case = int(input())
for _ in range(case):
    score = list(map(int, (input().split())))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1

    print("%.3f%%" % ((cnt/score[0])*100))
