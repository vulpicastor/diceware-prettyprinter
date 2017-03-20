#!/usr/env/python3
#
# Copyright 2017 Lizhou Sha
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Pretty prints the EFF diceware word lists so that it can be fed into
LP printers.

Author: Lizhou Sha <slz@mit.edu>
"""

import sys

ROW = 54
COL = 4
COL_WIDTH = 12
PAGEBREAK = "\f"

class PrettyPrinter(object):

    def __init__(self, row=ROW, col=COL, col_width=COL_WIDTH):
        self.row = row
        self.col = col
        self.col_width = col_width
        self.buffer = []
        self.buffer_max_len = row * col
        self.pages = []
        self.entry_format = "{:8}{:" + str(self.col_width) + "}"

    def __str__(self):
        return PAGEBREAK.join(self.pages)

    def add_line(self, line):
        index, word = line.strip().split()
        self.buffer.append((index, word))
        if len(self.buffer) == self.buffer_max_len:
            self.add_page()

    def add_page(self):
        if len(self.buffer) < self.buffer_max_len:
            return False
        page_buffer = []
        for cn in range(self.col):
            col = []
            page_buffer.append(col)
            for entry in self.buffer[self.row*cn:self.row*(cn+1)]:
                col.append(self.format_entry(entry))
        self.pages.append("\n".join(map("".join, zip(*page_buffer))))
        self.buffer = []
        return True

    def format_entry(self, entry):
        index, word = entry
        return self.entry_format.format(index, word)

def main():
    if len(sys.argv) == 5:
        row, col, col_width = sys.argv[2:5]
        pp = PrettyPrinter(row, col, col_width)
    elif len(sys.argv) < 2:
        raise ValueError("No file name given!")
    else:
        pp = PrettyPrinter()
    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            pp.add_line(line)
    print(pp)

if __name__ == "__main__":
    main()
