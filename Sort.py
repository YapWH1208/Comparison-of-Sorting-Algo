import time
import random
import sys
sys.setrecursionlimit(10**8)

class SortTest():
    def __init__(self):
        pass

    def main(self):
        size = [100,10000,50000,75000,100000,500000]
        functions = [self.selection_sort, self.merge_sort, self.quick_sort_v1, self.quick_sort_v2]
        for j in size:
            arr = self.generate_random_array(j)
            print(f"size: {j}")
            for i in functions:
                time_taken = self.test_function_time(i, arr)
                #sorted_array, time_taken = self.test_function_time(i, arr)
                print(i, time_taken)
                #print(i, sorted_array, time_taken, "\n")
            print("\n")

    def test_function_time(self,func, *args):
        start_time = time.time()
        func(*args)
        sorted_array = func(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time
        #return sorted_array, elapsed_time
    
    def generate_random_array(self,n):
        arr = [random.uniform(1,1000000) for _ in range(n)]
        return arr
    
    def selection_sort(self,arr):
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        #return arr
    
    def merge_sort(self,arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        #return arr

    def quick_sort_v1(self,arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = []
        right = []

        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])

        self.quick_sort_v2(left)
        self.quick_sort_v2(right)

        #left_sorted = self.quick_sort_v1(left)
        #right_sorted = self.quick_sort_v1(right)
        #return left_sorted + [pivot] + right_sorted

    def quick_sort_v2(self,arr):
        if len(arr) <= 1:
            return arr

        pivot = self.median_of_three(arr)
        left = []
        equal = []
        right = []

        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                right.append(arr[i])

        self.quick_sort_v2(left)
        self.quick_sort_v2(right)

        #left_sorted = self.quick_sort_v2(left)
        #right_sorted = self.quick_sort_v2(right)
        #return left_sorted + equal + right_sorted
    
    def median_of_three(self,arr):
        first = arr[0]
        last = arr[-1]
        middle_idx = len(arr) // 2
        middle = arr[middle_idx]

        return sorted([first, middle, last])[1]

SortTest().main()