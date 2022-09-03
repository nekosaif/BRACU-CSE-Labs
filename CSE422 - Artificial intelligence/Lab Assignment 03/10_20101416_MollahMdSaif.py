from random import sample


def a_b(a, b, k, l, p, idx):
    if l == 3: return p[idx]
    t = float('-inf') if k else float('inf')
    for i in [idx * 2, idx * 2 + 1]:
        s = a_b(a, b, not k, l+1, p, i)
        t, a, b = max(t, s) if k else min(t, s), (max(a, t) if k else a), (b if k else min(b, t))
        if a >= b: break
    return t


id = input('Enter your student ID\n').replace('0','8')
shuffles, rev, score_range = int(id[3]), int(id[-1:-3:-1]), range(int(id[4]), int(int(id[-1:-3:-1])*1.5))
players_lst = sample(score_range, 8)
score_point = a_b(float('-inf'), float('inf'), True, 0, players_lst, 0)
print('Generated 8 random points between the minimum and maximum point')
print(f'limits: {players_lst}')
print(f'Total points to win: {int(id[-1:-3:-1])}')
print(f'Achieved point by applying alpha-beta pruning = {score_point}')
if score_point >= rev:
    print('The winner is Optimus Prime\n')
else:
    print('The winner is Megatron\n')


score_lst = [a_b(float('-inf'), float('inf'), True, 0, sample(score_range, 8), 0) for _ in range(shuffles)]
print('After the shuffle:')
print(f'List of all points values from each shuffles: {score_lst}')
print(f'The maximum value of all shuffles: {max(score_lst)}')
print(f'Won {sum(s >= rev for s in score_lst)} times out of {shuffles} number of shuffles')
