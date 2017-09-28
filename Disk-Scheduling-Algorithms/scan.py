import os
import sys


def scan(filename):
    # initialize params
    fhandle = open(filename, "r")
    head = int(fhandle.readline().strip())
    task_str = fhandle.readline()
    task_list = task_str.strip().split(',')
    task_list = sorted([int(t) for t in task_list])
    schedule = []
    total_cost = 0
    min_track, max_track = 0, 199

    # split the task tracks into two parts: inside & outside the initial head
    inner_tracks, outer_tracks = [], []
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

    print ",".join([str(i) for i in schedule])
    print total_cost
    print str(schedule[-1]) + "," + str(total_cost)

def distance(src, tar):
    return abs(int(src) - int(tar))

def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    scan(sys.argv[1])

if __name__ == '__main__':
    main()