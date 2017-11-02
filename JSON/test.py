#! /usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import string
import sys

def stat_questions(file1, file2):
    count = 0
    q_list1 = []
    with open(file1, 'r') as f:
        for line in f:
            q_list1.append(line.strip().lower())

    q_list2 = []
    with open(file2, 'r') as f:
        for line in f:
            q_list2.append(line.strip().lower())

    print '==============================='
    for q1 in q_list1:
        if q1 not in q_list2:
            print q1
    print '==============================='
    for q2 in q_list2:
        if q2 not in q_list1:
            print q2 

# def test():
#     s = "I have_about    a.   !  / dream!"
#     arr = []
#     for c in string.punctuation:
#         s = s.replace(c, " ")
#         arr = s.split(" ")
#     arr = [i for i in arr if i.strip() != ""]
#     print arr

def main():
    # if len(sys.argv) != 3:
    #     print 'invalid parameters'
    #     exit(1)
    stat_questions(sys.argv[1], sys.argv[2])
    # test()

if __name__ == '__main__':
    main()