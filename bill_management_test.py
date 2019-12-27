# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:48:46 2019

@author: jmcau
"""

import unittest

from bill_management import BillManagement 

class TestBillManagement(unittest.TestCase):

    def test_read_bills2(self):
        bills = read_bills2()
        self.assertEqual(22, len(bills))
        self.assertEqual('Electric Ireland', bills[0][0])
        self.assertEqual('credit', bills[19][6])
        
    def test_insert_bill(self):
        insert = insert_bill()
        self.assertEqual

if __name__ == '__main__':
    unittest.main()