
for tc in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    #0 visit = [0] * (sum(score)+1) # 마지막에 중복제거

    #1 visit = [[0] * (sum(score)+1) for _ in range(N+1)]
    #2

    # def dfs(k,s):
    #     #1같은 높이에서 없애는것
    #
    #     if visit[k][s]: return
    #     visit[k][s] = 1

        #0 if k == N:
        #     print(s, end=" ")
        #     visit[s] = 1
        # else:
        #     dfs(k+1, s) #k번째 문제 틀린경우
        #     dfs(k+1, s+score[k]) # k번째 문제 맞은 경우

        #1 if k == N:
        #     return
        #
        # dfs(k+1, s) #k번째 문제 틀린경우
        # dfs(k+1, s+score[k]) # k번째 문제 맞은 경우


    #1 dfs(0,0)

    #2 whileq이용
    # visit = [0] * (sum(score) +1)
    # Q = [[0,0]] #k,s
    # while Q:
    #     k, s = Q.pop(0)
    #     if k == N:
    #         # print(s, end= " ")
    #         visit[s] = 1
    #     else:
    #         Q.append([k+1, s])
    #         Q.append([k+1, s + score[k]])
    #
    #
    # print(sum(visit))

    #상태공간트리느낌
    visit = [0] * (sum(score) + 1)

    Q = []

    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] +val]: continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)