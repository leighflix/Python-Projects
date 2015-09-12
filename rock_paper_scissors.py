import random

TARGET_POINTS = 3
MAP = {
    'p': 0,  # paper
    's': 1,  # scissors
    'r': 2,  # rock
}

print('First One To {} Points First Wins'.format(TARGET_POINTS))

player_score = 0
cpu_score = 0

while TARGET_POINTS not in (player_score, cpu_score):
    typed = input('(p)aper (s)cissors (r)ock: ')
    player = MAP[typed]
    cpu = random.randint(0, 2)
    result = (3 + player - cpu) % 3
    if result == 1:
        print('You win!')
        player_score += 1
    elif result == 2:
        print('You lost.')
        cpu_score += 1
    else:
        print('Tie.')
    print('Player: {} - PC: {}'.format(player_score, cpu_score))

if player_score == TARGET_POINTS:
    print('Game Over, You Win!')
if cpu_score == TARGET_POINTS:
    print('Game Over, You Lost.')
print('-=GAME OVER=-')
