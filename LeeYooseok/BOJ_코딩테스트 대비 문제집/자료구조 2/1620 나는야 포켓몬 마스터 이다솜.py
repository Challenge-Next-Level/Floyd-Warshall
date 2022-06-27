import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = dict()

for n in range(N):
    pokemon = input().rstrip()
    pokemon_dict[n + 1] = pokemon
    pokemon_dict[pokemon] = n+1
    
for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():
        print(pokemon_dict[int(problem)])
    else:
        print(pokemon_dict[problem])