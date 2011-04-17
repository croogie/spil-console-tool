#-*- coding: utf-8 -*-

from unittest import TestCase
import types

__author__ = 'Michał Świtoń'

class Version(object):
    def __init__(self, version_number, version_name = None):
        self.version_number = version_number
        self.version_name = version_name
        self.content = []

    def get_number(self):
        return self.version_number

    def set_number(self, number):
        self.version_number = number

    def get_name(self):
        return self.version_name

    def set_name(self, name):
        self.version_name = name

    def get_content(self):
        return self.content

    def replace_content(self, content):
        if type(content) is type([]):
            self.content = content
        else:
            self.content = content.splitlines()

    def clear_content(self):
        self.content = []

    def _get_lines_as_list(self, lines):
        if type(lines) is types.StringType:
            return lines.splitlines()
        
        if type(lines) is types.ListType:
            return lines
        
        return []

    def append_lines(self, lines):
        self.content += self._get_lines_as_list(lines)

    def prepend_lines(self, lines):
        self.content = self._get_lines_as_list(lines) + self.content

    def __str__(self):
        version = ['{0}-{1}'.format(self.get_name(), self.get_number())]
        version.append('-' * len(version[0]))
        version += self.get_content()
        version += ['']

        return '\n'.join(version)
