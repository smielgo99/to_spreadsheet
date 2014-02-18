# Portions Copyright (C) 2010, Manfred Moitzi under a BSD licence

from unittest import TestCase
import os
import sys

from xlrd import open_workbook
from xlrd.book import Book
from xlrd.sheet import Sheet

from base import from_this_dir

class TestWorkbook(TestCase):


    
    def setUp(self):
        self.book = open_workbook(from_this_dir('test.xlsx'))

    def test_open_workbook(self):
        self.assertTrue(isinstance(self.book, Book))

    def test_nsheets(self):
        self.assertEqual(self.book.nsheets, 2)

    def test_sheet_by_name(self):
        for name in self.sheetnames:
            sheet = self.book.sheet_by_name(name)
            self.assertTrue(isinstance(sheet, Sheet))
            self.assertEqual(name, sheet.name)

    def test_sheet_by_index(self):
        for index in range(2):
            sheet = self.book.sheet_by_index(index)
            self.assertTrue(isinstance(sheet, Sheet))
            self.assertEqual(sheet.name, self.sheetnames[index])

