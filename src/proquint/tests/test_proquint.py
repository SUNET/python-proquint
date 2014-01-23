#!/usr/bin/python
#
# Copyright (c) 2014 SUNET. All rights reserved.
# See the file LICENSE.md for full license statement.
#
# Author : Fredrik Thulin <fredrik@thulin.net>
#

"""
Test proquint generator.
"""

import socket
import struct
import unittest
import proquint


def _ip(ip):
    """
    Decode IP string to integer.
    """
    return struct.unpack('!I', socket.inet_aton(ip))[0]


def _b(data):
    """
    Decode binary string to integer.
    """
    return int(data.replace(' ', ''), 2)


class TestProquint(unittest.TestCase):

    def setUp(self):
        self.test_vectors = [
            (_ip('127.0.0.1'), 'lusab-babad'),
            (_ip('63.84.220.193'), 'gutih-tugad'),
            (_ip('63.118.7.35'), 'gutuk-bisog'),
            (_ip('140.98.193.141'), 'mudof-sakat'),
            (_ip('64.255.6.200'), 'haguz-biram'),
            (_ip('128.30.52.45'), 'mabiv-gibot'),
            (_ip('147.67.119.2'), 'natag-lisaf'),
            (_ip('212.58.253.68'), 'tibup-zujah'),
            (_ip('216.35.68.215'), 'tobog-higil'),
            (_ip('216.68.232.21'), 'todah-vobij'),
            (_ip('198.81.129.136'), 'sinid-makam'),
            (_ip('12.110.110.204'), 'budov-kuras'),
            (_b('0000 00 0000 00 0000 0000 00 0000 00 0000'), 'babab'),
            (_b('0000 00 0000 00 0000 0000 00 0000 00 0001'), 'babad'),
            (_b('0000 00 0000 00 0001 0000 00 0000 00 0001'), 'babad-babad'),
            (_b('1000 10 1000 10 1000 1000 10 1000 10 1000'), 'momom-momom'),
            (_b('1111 11 1111 11 1111 1111 11 1111 11 1111'), 'zuzuz-zuzuz'),
        ]

    def test_generation_1(self):
        """
        Test generating a proquint.
        """
        for (ip, expected) in self.test_vectors:
            self.assertEquals(expected, proquint.from_int(ip))

    def test_decoding_1(self):
        """
        Test decoding a proquint.
        """
        for (expected, pq) in self.test_vectors:
            self.assertEquals(expected, proquint.to_int(pq))
