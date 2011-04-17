__author__ = 'croogie'

import unittest
from version import Version

class VersionTest(unittest.TestCase):
    def test_empty(self):
        v = Version('7.1')
        self.assertEqual('7.1', v.get_number())
        self.assertEqual(None, v.get_name())
        self.assertEqual([], v.get_content())

    def test_modifying_lines(self):
        v = Version('7.1')

        v.replace_content(['1st line', '2nd line'])
        self.assertEqual('1st line', v.get_content()[0]) #check first line of content

        v.replace_content('3rd line\n4th line')
        self.assertEqual('3rd line', v.get_content()[0]) #check first line of content

        v.append_lines(['5th line', '6th line'])
        self.assertEqual('6th line', v.get_content()[-1]) #check if last element of content is '6th [...]'

        v.prepend_lines('zero line\nline to delete')
        self.assertEqual('line to delete', v.get_content()[1]) #check if second line is 'line to delete'

        v.clear_content()
        self.assertEqual(0, len(v.get_content()))

    def test_change_version_details(self):
        v = Version('7.1', 'gpconcept-family')

        self.assertEqual('7.1', v.get_number())
        self.assertEqual('gpconcept-family', v.get_name())

        v.set_name('gpcms-family')
        v.set_number('7.10')

        self.assertEqual('7.10', v.get_number())
        self.assertEqual('gpcms-family', v.get_name())

    def test_version_print(self):
        v = Version('7.1', 'test')
        v.replace_content('- linia pierwsza\n- linia druga')
        self.assertEqual('test-7.1\n--------\n- linia pierwsza\n- linia druga\n', v.__str__())

if __name__ == '__main__':
    unittest.main()
