import datetime
import os
import re
import time
from itertools import islice

import numpy as np
import pandas as pd
from BeautifulSoup import BeautifulSoup
from nltk.corpus import stopwords


def time_diff_str(t1, t2):
    """
    Calculates time durations.
    """
    diff = t2 - t1
    mins = int(diff / 60)
    secs = round(diff % 60, 2)
    return str(mins) + " mins and " + str(secs) + " seconds"


def clean_sentence(sentence):
    # Remove HTML
    review_text = BeautifulSoup(sentence).text

    # Remove non-letters
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    return letters_only


def convert_plain_to_csv(plain_name, tsv_name):
    t0 = time.time()
    with open(plain_name, "r") as f1, open(tsv_name, "w") as f2:
        i = 0
        f2.write("productId,score,summary,text\n")
        while True:
            next_n_lines = list(islice(f1, 9))
            if not next_n_lines:
                break

            # process next_n_lines: get productId,score,summary,text info
            # remove special characters from summary and text
            output_line = ""
            for line in next_n_lines:
                if "product/productId:" in line:
                    output_line += line.split(":")[1].strip() + ","
                elif "review/score:" in line:
                    output_line += line.split(":")[1].strip() + ","
                elif "review/summary:" in line:
                    summary = clean_sentence(line.split(":")[1].strip()) + ","
                    output_line += summary
                elif "review/text:" in line:
                    text = clean_sentence(line.split(":")[1].strip()) + "\n"
                    output_line += text

            f2.write(output_line)

            # print status
            i += 1
            if i % 10000 == 0:
                print( "%d reviews converted..." % i)
    print(" %s - Converting completed %s" % (datetime.datetime.now(), time_diff_str(t0, time.time())) )