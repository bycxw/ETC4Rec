from __future__ import print_function
import sys
import copy
import random
import numpy as np
from collections import defaultdict, Counter


def data_partition(fname):
    usernum = 0
    itemnum = 0
    User = defaultdict(list)
    user_train = {}
    user_valid = {}
    user_test = {}
    # assume user/item index starting from 1
    f = open(fname, 'r')
    for line in f:
        u, i = line.rstrip().split(' ')
        u = int(u)
        i = int(i)
        usernum = max(u, usernum)
        itemnum = max(i, itemnum)
        User[u].append(i)

    for user in User:
        nfeedback = len(User[user])
        if nfeedback < 3:
            user_train[user] = User[user]
            user_valid[user] = []
            user_test[user] = []
        else:
            user_train[user] = User[user][:-2]
            user_valid[user] = []
            user_valid[user].append(User[user][-2])
            user_test[user] = []
            user_test[user].append(User[user][-1])
    return [user_train, user_valid, user_test, usernum, itemnum]

def length_of_record(file_path):
    user_train, user_valid, user_test, usernum, itemnum = data_partition(file_path)
    seq_lens = defaultdict(int)
    for user in user_train:
        seq_lens[len(user_train[user]) // 100] += 1
    seq_lens = sorted(seq_lens.items(), key=lambda x: x[0], reverse=True)
    for i, (k, v) in enumerate(seq_lens):
        print(k, v, v / len(user_train))

if __name__ == "__main__":
    file_path = './data/ml-1m.txt'
    length_of_record(file_path)

