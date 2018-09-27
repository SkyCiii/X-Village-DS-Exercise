Question 1 Python的sorted跟sort()差別在哪?
Answer:

sorted()可以用在Class = list或Class = dict。他會建立一個新的list，然後把排序後的結果存入新的list並回傳值為listType，而不改變原list內的值。

sort()只能用在Class = list。且他不會建立新的list，而是在原本的list內做完排序，並回傳一個NoneType的值。

Question 2 Python是用哪種排序?
Answer:

Python是使用一種名為TimSort的演算法。TimSort是由MergeSort和InsertionSort組成。他的方法是把一個list內已經排序好的值取出來(Merge)，然後基於這些值，把其他未排序的值排序完成(Insertion)。