#!/usr/bin/env python

import random
import os
from random_file import id_generator
from random_file import string_generator
from random_file import date_generator

__author__ = 'stuart@cloudera.com'

out_file = open('file.out', 'w')
file_info = os.stat('file.out')
file_size = 0
count = 0

while (file_size < 1073741824):

    schema_file = open('table_schema.txt', 'r')
    for line in schema_file:
        line_array = line.split()
        column_name = line_array[0]
        column_type = line_array[1]
        if column_type == 'string':
            if column_name != 'evnt_crat_d':
                if column_name != 'blank_field_2':
                    s1 = (str(string_generator(random.randint(10,20))) + "|")
                    out_file.write(s1)

        if column_type == 'int':
            s2 = str(random.randint(1,1000))
            out_file.write(s2)
            out_file.write("|")

        if column_type == 'string':
            if column_name == 'evnt_crat_d':
                s3 = date_generator()
                out_file.write(s3)
                out_file.write("|")

        if column_type == 'string':
            if column_name == 'blank_field_2':
                s4 = (str(string_generator(random.randint(10,20))))
                out_file.write(s4)


        # year = str(random.randint(1980, 2014))
    # out_file.write(year)
    # out_file.write("|")
    # months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # month = (random.choice(months))
    # out_file.write(month)
    out_file.write("\n")

    file_info = os.stat('file.out')
    file_size = file_info.st_size
