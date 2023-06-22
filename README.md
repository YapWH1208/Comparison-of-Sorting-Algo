# Comparison-of-Sorting-Algo
Comparison of time complexity of different popular sorting algorithm

## Libraries Used
- time
- random
- os

## Sorting Algorithm Used
- Selection sort
- Merge sort
- Quick sort
  - Median of first, median, last number as the pivot
  - First number as the pivot
 
## Usage
```
python sort.py
```
## Average Result (in sec)
||100|10000|50000|75000|100000|500000|
|-|-|-|-|-|-|-|
|Selection Sort|0.00|1.38|43.65|108.12|196.91|5375.74|
|Merge Sort|0.00|0.01|0.11|0.16|0.24|1.33|
|Quick Sort (First)|0.00|0.01|0.08|0.11|0.17|1.02|
|Quick Sort (Median)|0.00|0.01|0.08|0.11|0.16|0.91|

## Enviroment
- Platform: Windows 11
- CPU: 12th Gen Intel(R) Core(TM) i7-12700H
- Memory: 16GB
- python: 3.10.8
