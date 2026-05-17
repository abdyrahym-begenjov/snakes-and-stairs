from random import randint
from time import sleep

p=['Player 2', 'Player 3', 'Player 4']
c=['COMPUTER1', 'COMPUTER2', 'COMPUTER3']

def game():
    name=input(f'[{p[0]}] Enter name: ')
    p.pop(0)
    if name =='':
        name=c[0]
        c.pop(0)
        return name
    return name

class Player:
    def __init__(self, name):
        self.name=name
        self.level=0
        self.status=5
        self.play=True

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.money_ice=1
        self.money_rocket=1
        self.money_teleport=1
        self.money_double=1
    def teleport(self, obj1):
        result=self.level
        self.level=obj1.level
        obj1.level=result
        self.money_teleport=0
        return self.level, obj1.level
    def rocket(self):
        self.level+=10
        self.money_rocket=0
        return self.level

class Computer(Player):
    pass

def ice(obj):
    obj.play=False
    return obj.play
def double(num):
    return num*2

print('Snakes and Stairs')
print('Creator: Abdyrahym Begenjov    (GitHub: abdyrahym-begenjov)')
start=input('Enter to start game: ', )
print('Loading...', )
sleep(2)
print('_'*100)

while True:
    count=input('Enter number of the players: ')
    if count in ('2', '3', '4'):
        count=int(count)
        break
    else:
        print('Error!!!')

snakes, lsnakes, stairs, lstairs, ssnake = [], [], [], [], []
print('Parametrs of game: Easy (50), Normal (75), Hard (100)')
while True:
    parametr=input('Enter the parametr of game: ')
    parametr=parametr.title().strip()
    match parametr:
        case 'Easy':
            parametr=50
            snakes=[13, 31]
            lsnakes=[47]
            stairs=[8, 38]
            lstairs=[22]
            break
        case 'Normal':
            parametr=75
            snakes=[25, 36, 49]
            lsnakes=[73, 68]
            stairs=[20, 38, 57]
            lstairs=[3, 12]
            break
        case 'Hard':
            parametr=100
            snakes=[24, 64, 63, 62]
            lsnakes=[13, 49, 80]
            stairs=[4, 32, 70, 61]
            lstairs=[15, 55, 87]
            ssnake=[95]
            break
        case _:
            print('Error!!!')

lst1=[]
while True:
    Player1=input('[Player 1] Enter name: ')
    if Player1!='':
        lst1.append(Player1)
        break
    else:
        print('Error!!!')

for i in range(count-1):
    x=game()
    lst1.append(x)

while True:
    lst=[]
    for i in lst1:
        move=randint(1, 6)
        lst.append((i, move))
    lst.sort(key=lambda x: x[1], reverse=True)    
    result=list(map(lambda x: x[1], lst))
    nr, r=[], []
    for i in result:
        if i not in nr:
            nr.append(i)
        else:
            r.append(i)
    if r==[]:
        print('Moment of Truth 🥁')
        match count:
            case 2:
                sleep(2)
            case 3:
                sleep(4)
            case 4:
                sleep(6)
        result=[f'{i}: {c}' for i, c in lst]
        text=', '.join(result)
        print(text)
        break
    else:
        continue

new_lst=list(map(lambda x: x[0], lst))
result1=[]
for i in new_lst:
    if i in ['COMPUTER1', 'COMPUTER2', 'COMPUTER3']:
        result1.append(Computer(i))
    else:
        result1.append(Human(i))

for n, i in enumerate(result1, 1):
    print(f'{n}) {i.name}')

start1=input('Enter to start game: ')
print('Let\'s Go!!!')
w=['First Winner', 'Second Winner', 'Third Winner', 'Forth Winner']
final_num=[1, 2, 3, 4]

def brosok(obj):
    isdouble=False
    isteleportation=False
    if obj.status==5 and obj.play!=False:
        if isinstance(obj, Human):
            while True:
                enter=input(f'[{obj.name}] Enter: ')
                match enter:
                    case 'teleport':
                        if obj.money_teleport==0:
                            print('NO')
                            isteleportation=False
                        else:
                            while True:
                                print('TELEPORTATION')
                                da_blin=input('Choose player for teleportation: ')
                                if da_blin==obj.name:
                                    print('Don\'t write your name!!!')
                                elif da_blin in [i.name for i in result1]:
                                    print(f'{obj.name} --> {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            obj.level, i.level=obj.teleport(i)
                                    break
                                else:
                                    print('Error!!!')
                            isteleportation=True
                        break
                    case 'double':
                        if obj.money_double==0:
                            print('NO')
                            isdouble=False
                        else:
                            print('DOUBLE')
                            obj.money_double=0
                            isdouble=True
                    case 'rocket':
                        if obj.money_rocket==0:
                            print('NO')
                        elif obj.level+10>=parametr:
                            print('NO')
                        else:
                            print('ROCKET   +10')
                            obj.level=obj.rocket()
                    case 'ice':
                        if obj.money_ice==0:
                            print('NO')
                        else:
                            while True:
                                da_blin=input('Choose player for ice: ')
                                if da_blin==obj.name:
                                    print('Don\'t write your name!!!')
                                elif da_blin in [i.name for i in result1]:
                                    print(f'ICE: {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            i.play=ice(i)
                                    obj.money_ice=0
                                    break
                                else:
                                    print('Error!!!')
                    case _:
                        break
        if isteleportation==False:
            if isinstance(obj, Computer):
                print(f'[{obj.name}] Generate: ')
            num=randint(1, 6)
            if isdouble==True:
                print(f'{num}x2')
                num=double(num)
            print(f'{num}')
            obj.level+=num
            if obj.level==parametr:
                print(obj.level)
                obj.status=final_num[0]
                print(w[0])
                final_num.pop(0)
                w.pop(0)
            elif obj.level>parametr:
                print('Number is bigger than parametr')
                obj.level-=num
                print(obj.level)
            elif obj.level in snakes:
                print('🐍')
                obj.level-=6
                print(obj.level)
            elif obj.level in lsnakes:
                print('🐍🐍')
                obj.level-=12
                print(obj.level)
            elif obj.level in ssnake:
                print('Dangerous 🐍')
                obj.level-=60
                print(obj.level)
            elif obj.level in stairs:
                print('🪜')
                obj.level+=6
                print(obj.level)
            elif obj.level in lstairs:
                print('🪜🪜')
                obj.level+=12
                print(obj.level)
            else:
                print(obj.level)
        else:
            print(obj.level)
        spisok2_result=(obj.level, obj.status)
    elif obj.play==False:
        print(f'{obj.name} is iced!')
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result

while True:
    for player in result1:
        player.level, player.status=brosok(player)
        player.play=True
    spisok=[]
    for player in result1:
        spisok.append((player.name, player.level, player.status))
    spisok.sort(key=lambda x: x[2], reverse=False)
    spisok1=list(map(lambda x: x[0], spisok))
    spisok2=list(map(lambda x: x[2], spisok))
    if 1 in spisok2 and count==2:
        print(f'1) {spisok1[0]} - WINNER 😎🏆')
        print(f'2) {spisok1[1]} - LOSER 😫')
        break
    elif 1 in spisok2 and 2 in spisok2 and count==3:
        print(f'1) {spisok1[0]} - WINNER 😎🏆')
        print(f'2) {spisok1[1]} - ROUND-UP 😀')
        print(f'3) {spisok1[2]} - LOSER 😫')
        break
    elif 1 in spisok2 and 2 in spisok2 and 3 in spisok2 and count==4:
        print(f'1) {spisok1[0]} - WINNER 😎🏆')
        print(f'2) {spisok1[1]} - ROUND-UP 😀')
        print(f'3) {spisok1[2]} - BRONZE MEDALIST 😐')
        print(f'4) {spisok1[3]} - LOSER 😫')
        break

end=input('Enter to exit: ')