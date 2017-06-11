import heapq
from headpq_showtree import show_tree
from heapq_heapdata import data
print('random:', data)
heapq.heapify(data)
print('heapified')
show_tree(data)
