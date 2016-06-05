__author__ = 'Kalyan'

from placeholders import *


profiling_timeit = '''
Python also gives a helpful timeit module that can be used for benchmarking a given piece of code

Reading material:
 http://docs.python.org/2/library/timeit.html
 http://stackoverflow.com/questions/8220801/how-to-use-timeit-correctly
 http://www.dreamincode.net/forums/topic/288071-timeit-module/

Try out on sample code snippets from above links on your own before you get to the assignment.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using timeit in this assignment.

for each value of count, execute the method 5 times using timeit and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

'''

from unit7_conversion_methods import *
import timeit

def profile_timeit():
    func=[numbers_string1,numbers_string2,numbers_string3,num_strings4]
    for x in func:
        for count in (10,100,1000,1000):
            time_list=[]
            for y in range(5):
                time_list.append(round(timeit.timeit(setup=x(count),number=10000),4))
            print x.__name__+", "+"count= "+str(count)+" min = "+ str(min(time_list))+", actuals= "+str(time_list)
    pass
# write your findings on what you learnt about timeit, measuring perf and how the results here compare to
# values in assignment1
summary = '''
timeit lets us compare between very small time frames
while in assignment1 time.clock() used to give difference between interval of clock between two calls
timeit act as more precise way of comparision
'''

if __name__ == "__main__":
    profile_timeit()
