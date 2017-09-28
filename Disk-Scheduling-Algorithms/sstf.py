import os
import sys

def sstf(filename):
    fhandle = open(filename, "r")
    head = int(fhandle.readline().strip())
    task_str = fhandle.readline()
    task_list = task_str.strip().split(',')
    task_list = sorted([int(t) for t in task_list])
    schedule = []
    total_cost = 0

    while len(task_list) > 0:
        distance_list = sorted([distance(head, t) for t in task_list])
        min_dist = distance_list[0]
        if head - min_dist in task_list: # if there is a tie, move at the direction towards innermost first
            schedule.append(head - min_dist)
            head = head - min_dist
        elif head + min_dist in task_list:
            schedule.append(head + min_dist)
            head = head + min_dist

        total_cost += min_dist
        task_list.remove(head)

    print ",".join([str(i) for i in schedule])
    print total_cost
    print str(schedule[-1]) + "," + str(total_cost)

    fhandle.close()

def distance(src, tar):
    return abs(int(src) - int(tar))

def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    sstf(sys.argv[1])

if __name__ == '__main__':
    main()