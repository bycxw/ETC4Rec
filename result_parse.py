# coding: utf-8
"""
parse log file
"""
import re
from collections import namedtuple, defaultdict

OneMetric = namedtuple("OneMetric", ["name", "value"])

metric_pattern = re.compile(r"(ndcg@1)|(ndcg@5)|(ndcg@10)|(hit@1)|(hit@5)|(hit@10)")


def log_parse(metric_pattern, log_file_path):
    result = defaultdict(list)
    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            global_step = parse_global_step(line)
            one_metric = parse_metrics(metric_pattern, line)
            if one_metric:
                result[global_step].append(one_metric)
        print_result(result)


def print_result(result):
    for step in result:
        print(step)
        for one_metric in result[step]:
            print(one_metric.name, one_metric.value)


def parse_global_step(line):
    if "Restoring parameters" in line:
        global_step =int(line.split("/")[-1].split("-")[-1])
        return global_step
    else:
        return


def parse_metrics(metric_pattern, line):
    if re.search(metric_pattern, line):
        name, value = line.split(":")
        return OneMetric(name, value)
    else:
        return


if __name__ == "__main__":
    log_file_path = "c:/Data/dissertation/record/ml-25m-500-mp1.0-sw0.5-mlp0.2-df10-mpps40-msl200-ts200000-64/nohup.out"
    log_parse(metric_pattern, log_file_path)