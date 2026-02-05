#pure functions

def pure_func(hell):
    return hell + 89
total_chai = 0

#not recommended impure functions
def impure_func(hell):
    global total_chai
    total_chai += cups
    pass

#recursive function
def rec_func(h,i=0):
    
    print(f"{i+1}\n")
    
    if h==0:
        return "waht is the number"
    return rec_func(h-1, i+1)

print(rec_func(4))

#Lambdas

whatIs = ['box','pencil','ink','box']

answerEasy = list(filter(lambda instrumemt: instrumemt == 'box',whatIs))

print(answerEasy)