__author__ = 'croogie'

import unittest
from parser import Parser

class ParserTest(unittest.TestCase):
    files = {
        'one_entry' : '../../test_files/UPGRADE_1.txt',
        'many_entries' : '../../test_files/UPGRADE_2.txt'
    }

    def test_empty(self):
        dp = Parser()
        self.assertEqual([], dp.get_content())
        self.assertEqual(None, dp.get_version_numbers())
        self.assertEqual(None, dp.get_version('7.1'))

    def test_one_entry_file(self):
        dp = Parser(self.files['one_entry'])

        self.assertEqual(7, len(dp.get_content())) # file should have 7 lines
        self.assertEqual('7.1', dp.get_version_numbers()[0]) # first and only one version is 7.1
        self.assertEqual('gpconcept-family', dp.get_version('7.1').get_name()) # name of 7.1 version is 'gpconcept-family'
        self.assertEqual(None, dp.get_version('7.2')) # there is no version like 7.2 - None should be returned
        self.assertEqual(5, len(dp.get_version('7.1').get_content())) # version 7.1 should have 5 lines
        self.assertEqual('- Second line', dp.get_version('7.1').get_content()[1]) # second line of version should contain...

    def test_sorted_order(self):
        dp = Parser(self.files['many_entries'])
        self.assertEqual(['7.10', '7.9.2', '7.9.1', '7.9'], dp.get_version_numbers())


if __name__ == '__main__':
    unittest.main()
