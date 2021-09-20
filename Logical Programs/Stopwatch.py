"""
Header Section
@Author: Anil
@Date: 2021-09-12 9:50
@Last Modified by: Anil
@Last Modified time: 2021-09-12 10:10
@Title : Stopwatch Program
"""
import time
input("Press enter to start time")
start_time = time.time()
input("Press enter to end time")
end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed is : ",elapsed_time)