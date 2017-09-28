import os
import sys
import copy

min_track, max_track = 0, 199

def fscan(filename):
    # initialize params
    fhandle = open(filename, "r")
    head = int(fhandle.readline().strip())
    task_str = fhandle.readline()
    task_list = task_str.strip().split(',')
    if len(task_list) == 0:
        return []

    schedule = []
    total_cost = 0
    q1 = []
    q2 = []

    while True:
        q1, q2, task_list = move_queue(q1, q2, task_list)
        if not task_list and not q1:
            break
        
        head, cur_cost, q1 = scan(head, q1)
        schedule.extend(q1)
        # print schedule
        total_cost += cur_cost
        
    print ",".join([str(i) for i in schedule])
    print total_cost
    print str(schedule[-1]) + "," + str(total_cost)
    fhandle.close()

def scan(head, task_list):
    total_cost = 0
    inner_tracks, outer_tracks = [], []
    task_list = sorted([int(t) for t in task_list])
    schedule = []
    total_cost = 0
    for t in task_list:
        if t > head:
            outer_tracks.append(t)
        else:
            inner_tracks.append(t)
    if len(outer_tracks) == 0:
        schedule.extend(reversed(inner_tracks))
        total_cost = head - schedule[-1]
    elif len(inner_tracks) == 0:
        schedule.extend(outer_tracks)
        total_cost = schedule[-1] - head
    elif distance(head, outer_tracks[0]) < distance(head, inner_tracks[-1]):  # move outside
        schedule.extend(outer_tracks)
        schedule.extend(reversed(inner_tracks))
        total_cost = (max_track - head) + (max_track - inner_tracks[0])
    else:
        schedule.extend(reversed(inner_tracks))
        schedule.extend(outer_tracks)
        total_cost = (head - min_track) + (outer_tracks[-1] - min_track)
    head = schedule[-1]

    return head, total_cost, schedule

def distance(src, tar):
    return abs(int(src) - int(tar))

def move_queue(q1, q2, task_list):
    if q1:
        q1 = q2
    else:   # initialization case
        q1 = task_list[:10]
    if q2: 
        q2 = task_list[:10]
        task_list = task_list[10:]
    else:   # initialization case
        q2 = task_list[10:20]
        task_list = task_list[20:]

    return q1, q2, task_list

def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    fscan(sys.argv[1])

if __name__ == '__main__':
    main()