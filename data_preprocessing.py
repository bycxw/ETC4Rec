# coding: utf-8

"""
Preprocess the raw data.
"""

import os

from collections import namedtuple, defaultdict
from tqdm import tqdm


def ml_preprocess(in_file_path, out_file_path, min_rating_num=0):
    OneRating = namedtuple("OneRating", ["movieid", "timestamp"])
    ratings = defaultdict(list)
    print("Start processing {}.".format(in_file_path))
    with open(in_file_path, "r", encoding="utf-8") as in_f, open(out_file_path, "w", encoding="utf-8") as out_f:
        header = in_f.readline()
        last_userid = "1"
        cnt = 0
        for line in tqdm(in_f):
            cnt += 1
            line = line.strip().split(",")
            userid, movieid, rating, timestamp = line
            ratings[userid].append(OneRating(movieid, timestamp))
            if userid != last_userid:
                if cnt >= min_rating_num:
                    sorted_ratings = sorted(ratings[last_userid], key=lambda one_rating: one_rating.timestamp)
                    for one_rating in sorted_ratings:
                        out_f.write("{},{}\n".format(last_userid, one_rating.movieid))
                last_userid = userid
                cnt = 1
        print("Done")
        print("Processed file: {}".format(out_file_path))


if __name__ == "__main__":
    MIN_RATING_NUM = 0
    in_file_path = os.path.join("..", "datasets", "ml-25m", "ratings.csv")
    out_file_path = os.path.join("data", "ml-25m-{}.txt".format(MIN_RATING_NUM))
    ml_preprocess(in_file_path=in_file_path,
                  out_file_path=out_file_path,
                  min_rating_num=MIN_RATING_NUM)