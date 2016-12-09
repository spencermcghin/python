#! /usr/bin/env python3

""" Imports """

import pandas as pd

""" Classes """

class Data(object):

    def __init__(self, data):

        self.data = pd.DataFrame(pd.read_csv(open(file, 'rt')))
        self.dim = data

    # Upload file and convert to data frame object

    def group_by_sum(self):

