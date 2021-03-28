# coding: utf-8

"""
Preprocess the raw data.
"""

import os

from collections import namedtuple, defaultdict
from pathlib import Path
from tqdm import tqdm

class UserItemVocab(object):
    def __init__(self):
        self.user = dict()
        self.item = dict()

    def update_user(self, user):
        if user not in self.user:
            self.user[user] = len(self.user) + 1

    def update_item(self, item):
        if item not in self.item:
            self.item[item] = len(self.item) + 1

    def convert_user_to_id(self, user):
        return self.user.get(user, None)

    def convert_item_to_id(self, item):
        return self.item.get(item, None)

    def get_user_count(self):
        return len(self.user)

    def get_item_count(self):
        return len(self.item)



def process_raw_ml(in_file_path: Path, out_file_path: Path, min_rating_num: int = 0):
    """
    process raw movielens ratings data. One line represents one interaction by one user and has the following format:
        userId,movieId
    The lines within user are ordered by timestamp.

    in_file_path: path like. movielens ratings file
    out_file_path: path like. processed file
    min_rating_num: int. minimum interactions by one user. Interactions less than min_rating_num would be filtered.
    """
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
        print("Process raw ml data done.")
        print("Processed file: {}".format(out_file_path))

def build_vocab(file_path: Path):
    """
    Build vocab for interaction data.
    """
    print("Start build vocab...")
    vocab = UserItemVocab()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(",")
            user, movie = line
            vocab.update_user(user)
            vocab.update_item(movie)
    print("Build vocab done.")
    print("user num: {}, item num: {}".format(vocab.get_user_count(), vocab.get_item_count()))
    return vocab


def build_data(in_file_path: Path, out_file_path: Path, vocab: UserItemVocab):
    """
    build data for model.
    Convert user/item name to id.
    """
    print("Start build data...")
    with open(in_file_path, "r", encoding="utf-8") as in_f, open(out_file_path, "w", encoding="utf-8") as out_f:
        for line in in_f:
            line = line.strip().split(",")
            user, movie = line
            user_id, movie_id = vocab.convert_user_to_id(user), vocab.convert_item_to_id(movie)
            if not user_id or not movie_id:
                continue
            out_f.write("{} {}\n".format(user_id, movie_id))
    print("Build data done.")
    print("data file: {}".format(out_file_path))


def ml_preprocess(in_file_path: Path, out_file_path: Path, min_rating_num: int = 0):

    tmp_file_path = Path(out_file_path.parent, out_file_path.name + ".tmp")
    process_raw_ml(in_file_path=in_file_path, out_file_path=tmp_file_path, min_rating_num=min_rating_num)
    vocab = build_vocab(file_path=tmp_file_path)
    build_data(in_file_path=tmp_file_path, out_file_path=out_file_path, vocab=vocab)
    os.remove(tmp_file_path)


if __name__ == "__main__":
    MIN_RATING_NUM = 0
    in_file_path = Path("..", "datasets", "ml-25m", "ratings.csv")
    out_file_path = Path("..", "datasets", "ml-25m", "ml-25m-{}.txt".format(MIN_RATING_NUM))
    ml_preprocess(in_file_path=in_file_path,
                  out_file_path=out_file_path,
                  min_rating_num=MIN_RATING_NUM)