# -*- coding: utf-8 -*-
"""
PFOS_Histogram generates a histogram by principal field of science (PFOS) from
data exported from the PSC Portal (Staff > Bridges > Project Requests).

The input file is 'PSC_User_Portal.csv'.

The output file is 'PFOS_Histogram.csv', where each row consists of the
following columns:
1. NFS numerical code for the principal field of science. For example,
   412 corresponds to "Biophysics", 330 corresponds to "Computer and
   Information Science and Engineering", and 440 corresponds to "Behavioral
   and Neural Sciences".
2. NFS name for the principal field of science, e.g., "Biophysics",
   "Computer and Information Science and Engineering", and "Behavioral and
   Neural Sciences".
3. The number of occurrences of that principal field of science in the input
   data.

The rows are sorted by the first column (NFS numerical code for the PFOS) to
reflect grouping of similar fields of science, to the extent that the NFS
system supports it.

@author: Nick Nystrom
@version: 1.0
"""

"""

"""

__author__ = "Nick Nystrom"
__version__ = 0.1

import csv
import re

pfos = {}
re_get_pfos = re.compile('\d{1,3}')
re_remove_pfos_code = re.compile(' \(\d{1,3}\)')

with open('PSC_User_Portal.csv', newline='', encoding='utf-8') as ifile:
    reader = csv.reader(ifile)
    irow = 0
    for row in reader:
        irow = irow + 1
        if (irow > 1):
            pfos_code = re_get_pfos.search(row[10]).group()
            pfos_name = re_remove_pfos_code.sub('',row[10])
            if pfos_code in pfos:
                pfos[pfos_code] = (pfos_name, pfos[pfos_code][1]+1)
            else:
                pfos[pfos_code] = (pfos_name, 1)

with open('PFOS_Histogram.csv', 'w', newline='') as ofile:
    writer = csv.writer(ofile, delimiter=',')
    for p in sorted(pfos):
        v = pfos[p]
        t = [p,v[0],v[1]]
        # print(t)
        writer.writerow(t)