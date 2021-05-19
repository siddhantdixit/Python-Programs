import matplotlib.pyplot as plt
import numpy
import time

''' O(N) '''
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

''' O(N^2) '''
def my_func(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        for y in range(1,i+1): 
            s = s + i
    end_time = time.time()
    return s,end_time-start_time


n_x = list()
time_y = list()
i = 2
while i<=10000:
    ans = my_func(i)
    n_x.append(i)
    time_y.append(ans[1])
    # i = int(i*1.5)
    i*=2

print(n_x)
print(time_y)
plt.style.use('dark_background')
plt.plot(n_x,time_y)
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.title("Time Complexity of Function")
plt.show()
