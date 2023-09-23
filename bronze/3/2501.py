measure_list = []
n, k = map(int, input().split()) 


for i in range(1, n+1):
    if n % i == 0:
        measure_list.append(i)
        
      
if k > len(measure_list):
    print(0)
else:
    print(measure_list[k-1])