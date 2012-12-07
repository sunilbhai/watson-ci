# -*- coding: utf-8 -*-

import its
import mox

try:
    import unittest2 as unittest
except ImportError:
    if not its.py27:
        raise
    import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()

    def tearDown(self):
        self.mox.UnsetStubs()
        self.mox.ResetAll()
