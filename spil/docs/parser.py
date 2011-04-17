#-*- coding: utf-8 -*-

from os import path
import re
from unittest import TestCase
from version import Version
from distutils import version

__author__ = 'croogie'

class Parser(object):
    rVersionHeader = re.compile('^\s*([\w-]+)-([\d\.]+){1}\s*$') # regex to get version header
    rLine = re.compile('^\s*\-+\s*$') # regex to get line
    rEmptyLine = re.compile('^\s*$') # regex to get empty line

    def __init__(self, filename=None):
        self.content = []
        self.versions = {}
        self.parsed = False
        self.filename = None

        if filename != None:
            self._open_file(filename)


    def get_content(self):
        """Gets all file content (as list)"""
        return self.content

    def _open_file(self, filename):
        """Opens file, remembers file name, parse file content"""
        if (path.exists(filename) and path.isfile(filename)):
            file = open(path.abspath(filename))
            self.filename = filename
            self.content = file.readlines()
            self._parse_content()
            file.close()

    def compare_versions(self, x, y):
        a = version.StrictVersion(x)
        b = version.StrictVersion(y)
        if (a > b):
            return 1
        elif (a < b):
            return -1
        else:
            return 0

    def get_version_numbers(self):
        """Gets version numbers"""
        if self.parsed is True:
            ver = self.versions.keys()
            ver.sort(cmp=self.compare_versions, reverse=True)
            return ver

        return None

    def _parse_content(self):
        """Parse content of DOC file"""
        if len(self.content) > 0:
            current_version = None

            for line in self.content:
                #check if line is version header
                matched_line = self.rVersionHeader.match(line)
                if matched_line is not None:
                    self.versions[matched_line.group(2)] = Version(matched_line.group(2), matched_line.group(1))
                    current_version = matched_line.group(2)
                else:
                    if current_version is not None and self.rLine.match(line) is None and line.strip() is not '':
                        self.versions[current_version].append_lines(line)

            self.parsed = True

    def get_version(self, version_number):
        """Get specified version number (if exists). Otherwise None will be returned"""
        if self.parsed is True and self.versions.has_key(version_number):
            return self.versions.get(version_number)
        return None

    def __str__(self):
        result = []
        for version in self.get_version_numbers():
            result.append(self.get_version(version).__str__())
        return '\n'.join(result)
