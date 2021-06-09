import time
import random


def progress(percent, width=50):
    if percent > 1:
        percent = 1
    show_wtr = ('[%%-%ds]' % width) % ('#' * int(percent * width))
    print('\r', show_wtr, 100 * percent, '%', end='')


recv_size = 0
total_size = 99999
while recv_size < total_size:
    t = random.random()
    time.sleep(t)
    recv_size += 1024
    progress(recv_size / total_size)
