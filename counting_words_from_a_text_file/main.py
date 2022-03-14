import string
#It's not necessary if you can remember the all punctuation marks that are there in Grammar.
#Which I can't remember so I have used `string.punctuation = !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~`


                   #-------------------------------------------------#
                   #      This is from where code starts             #
                   #-------------------------------------------------#

                   
def test(String):  #This function removes words having punction on it's end
    #Say `String = Well,` so this will return only `Well`
    #Similarly, if `Wooww!` >>> `Wooww` The exclamation in the end will be removed.
    for x in string.punctuation:
        String = String.strip(x)
    return String



with open('path.txt') as f:
    lst =[test(word) for line in f for word in line.split()]




stor, ans = [], []
for x in lst:
    if x not in stor:
        stor.append(test(x))
        ans.append((x, lst.count(x)))

        
ans.sort(key = lambda x: x[0].lower(), reverse = True) #You can remove this True
#The above line sorts the words as taking as lower order
#The below line sorts words as per their counts
#Word with the highest count will be the first word
ans.sort(key = lambda x: x[1], reverse = True)


#Storing the counts of each word in a .txt
with open('store_path.txt', 'a') as Store:
    for x in ans:
        Store.write(f'{x[0]} {x[1]}\n')

