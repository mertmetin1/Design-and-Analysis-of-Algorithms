
import time
def coinrow(array):
    n=len(array)
    temp=[0]* n
    temp[0]=array[0]
    temp[1]=array[1]
    for i in range(2,n,1):
        temp[i]=max(array[i]+temp[i-2],temp[i-1])
    return temp[n-1]

def coinrowtail(array, i):
    if i == 0:
        return array[0]
    elif i == 1:
        return max(array[0], array[1])
    else:
        prev = coinrowtail(array, i - 1)
        prev2 = coinrowtail(array, i - 2)
        return max(prev2 + array[i], prev)

def coinrowRec(array):
    return coinrowtail(array, len(array) - 1)

a = [1, 0, 0, 0, 1, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
start_time = time.time() # Başlangıç zamanını al
coinrowRec(a)
end_time = time.time() # Bitiş zamanını al
elapsed_time = end_time - start_time # Geçen süreyi hesapla
print(coinrowRec(a),": Recursive          :", elapsed_time*100, "s")


start_time1 = time.time() # Başlangıç zamanını al
coinrow(a)
end_time1 = time.time() # Bitiş zamanını al
elapsed_time = end_time1 - start_time1 # Geçen süreyi hesapla
print(coinrow(a),": Dynamic Programming:", elapsed_time*100, "s")
