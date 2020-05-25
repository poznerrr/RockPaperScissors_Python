import random

def comparing(myfeel, _rating, _variants):
    compfeel = random.choice(_variants)
    if myfeel == compfeel:
        print('There is a draw ({})'.format(compfeel))
        return _rating + 50
    else:
        myposition = _variants.index(myfeel)
        resultlist = _variants[myposition+1:]
        resultlist.extend(_variants[:myposition])       
        if compfeel in resultlist[:len(resultlist)//2]:
            print('Sorry, but computer chose {}'.format(compfeel))
            return _rating
        print('Well done. Computer chose {} and failed'.format(compfeel))
        return _rating + 100
def refile(_file_name, _name, _rating):
    file = open(_file_name,'r')
    ratelist = file.readlines()
    file.close()
    ratelist = [x.strip('\n') for x in ratelist]
    for cur_rate in ratelist:
        if _name in cur_rate:
            ratelist.remove(cur_rate)
    ratelist.append(f'{_name} {_rating}')
    file = open(_file_name,'w')
    for line in ratelist:
        file.write(line+'\n')
    file.close()

my_name = input("Enter your name: ")
print(f'Hello, {my_name}')
my_rating = 0
variants = input("Please, enter possible variants: ").split(',')
if variants == ['']:
    print('Game will start with default variants: rock, paper, scissors')
    variants = ['rock', 'paper', 'scissors']
#working with file
#if file not created:
file = open('rating.txt','a')
file.close()
print("Okay, let's start")
file = open('rating.txt','r')
rate = file.readlines()
file.close()
rate = [x.strip('\n') for x in rate]
for line in rate:
    if my_name == (line.split())[0]:
        my_rating = int((line.split())[1])
while True:    
    my_choose = input()
    if my_choose in variants:
        my_rating = comparing(my_choose, my_rating, variants)     
        refile('rating.txt', my_name, my_rating)
    elif my_choose == '!exit':
        print('Bye!')
        break
    elif my_choose =='!rating':
        print(f'Your rating: {my_rating}')
    else:
        print('Invalid input')
