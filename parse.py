#!/usr/bin/python3

import csv
import sys

if len(sys.argv) < 2:
        print("Provide CSV file")
        exit()

db_list = []
mcc_codes = {}

sorted_list = {}

with open('mcc_codes.csv', newline='') as mccfile:
        reader = csv.reader(mccfile)
        for row in reader:
                try:
                        code = int(row[0])
                except:
                        continue

                mcc_codes[code] = row[1]

def add_dollars(a, b):
        if (a[0] == '-'):
                _a = round(float(a[1:-1].strip('$'))) * -1
        else:
                _a = round(float(a.strip('$')))

        if (b[0] == '-'):
                _b = round(float(b[1:-1].strip('$'))) * -1
        else:
                _b = round(float(b.strip('$')))

        res = round(_a + _b, 2)

        res = '$' + str(res)

        return res

with open(sys.argv[1], newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
                tup = (row[0], row[1], row[2])
                try:
                        code = int(tup[1].split(' ')[-1])
                except:
                        continue

                if sorted_list.get(code, None) is None:
                        sorted_list[code] = (mcc_codes[code], tup[2])
                else:
                        new = add_dollars(sorted_list[code][1], tup[2])
                        sorted_list[code] = (mcc_codes[code], new)

print("----------------------- Summary ---------------------------")

total = 0.0

for idx in sorted_list:
        print("%s      \t%s" % (sorted_list[idx][1], sorted_list[idx][0]))
        total += float(sorted_list[idx][1].strip('$'))
        round(total, 2)

total = round(total, 2)
print("-----------------------------------------------------------")
print("$%s    \tTotal Spent" % str(total))