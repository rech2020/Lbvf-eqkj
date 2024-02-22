from itertools import permutations
from random import *



words = []
correct_words_set = set()

with open('Ударения.txt', encoding="utf-8") as f:
    for word in f:
        words.append(''.join(word.split()))
        correct_words_set.add(''.join(word.split()))
correct_words = {key: value for value, key in enumerate(sorted(words), 1001)}




vowels_const = set("АЕЁИОУЫЭЮЯаеёиоуыэюя")
words = set()
all_words_set = set()

for word in correct_words.keys():
    word = list(word)
    count = 0
    for letter in word:
        if letter in vowels_const:
            count += 1
    commands = '2' + '1'*(count-1)
    for permutation in permutations(commands):
        count = 0
        for i in range(len(word)):
            if word[i] in vowels_const:
                if permutation[count] == '1':
                    word[i] = word[i].lower()
                if permutation[count] == '2':
                    word[i] = word[i].upper()
                count += 1
        words.add(''.join(word))
        all_words_set.add(''.join(word))
all_words = {key: value for value, key in enumerate(sorted(words), 1)}



incorrect_words_set = all_words_set - correct_words_set
incorrect_words = {key: value for value, key in enumerate(sorted(incorrect_words_set), 2001)}
print(all_words)
print(correct_words)
print(incorrect_words)




for i in range(1,20):
    problem = sample(list(all_words_set), 5)
    count = 0
    keys = set()
    for word in problem:
        if word in correct_words_set:
            count += 1
        keys.add(words.lower())
    if count > 0 and len(keys)==5:
        with open(f'D:/Рабочий стол/Задания №2/Problems/Problem №{i}.txt', 'w+', encoding='utf-8') as p:
            for word in problem:
                p.writelines(word+'\n')
        with open(f'D:/Рабочий стол/Задания №2/Answers/Answer №{i}.txt', 'w+', encoding='utf-8') as a:
            for word in problem:
                if word in correct_words:
                    a.writelines(str(correct_words[word])+'\n')
                if word in incorrect_words:
                    a.writelines(str(incorrect_words[word])+'\n')
#print(base)
        
    


                
            
        
    
