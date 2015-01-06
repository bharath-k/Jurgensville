#
# Copyright (c) 2013 D. E. Shaw & Co., L.P. All rights reserved.
#
# This software is the confidential and proprietary information
# of D. E. Shaw & Co., L.P. ("Confidential Information").  You
# shall not disclose such Confidential Information and shall use
# it only in accordance with the terms of the license agreement
# you entered into with D. E. Shaw & Co., L.P.
#

from __future__ import (print_function, absolute_import, division,
                        with_statement)
import unittest
import subprocess

class TestRestaurant(unittest.TestCase):
    """
    A few basic tests for service director.
    """
    def __init__(self, methodName):
        return super(TestRestaurant, self).__init__(methodName)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _execute(self, input, expected, testcase):
        command = ["/usr/local/bin/python", "../best-price.py"] + input
        proc = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=False)
        (stdoutdata, stderrdata) = proc.communicate()
        self.assertFalse(proc.returncode)
        self.assertFalse(stderrdata)
        self.assertEquals(stdoutdata.strip(), expected, "Test case %s failed" % testcase)

    def test_data1_1(self):
        """
        $ python best-price.py data1.csv burger
        1 , 4.0
        """
        self._execute(["data1.csv", "burger"], "1 , 4.0", "data1_1")

    def test_data1_2(self):
        """
        $ python best-price.py data1.csv burger tofu_log
        2 , 11.5
        """
        self._execute(["data1.csv", "burger", "tofu_log"], "2 , 11.5", "data1_2")

    def test_data2(self):
        """
        $ python best-price.py data2.csv chef_salad wine_spritzer
        No restaurants found for given menu item(s).
        """
        self._execute(["data2.csv", "chef_salad", "wine_spritzer"], "No restaurants found for given menu item(s).", "data2")

    def test_data3(self):
        """
        $ python best-price.py data3.csv fancy_european_water extreme_fajita
        6 , 11.0
        """
        self._execute(["data3.csv", "fancy_european_water", "extreme_fajita"], "6 , 11.0", "data3")

    def test_data4(self):
        """
        # value in combo is lesser
        $ python best-price.py data4.csv burger
        2 , 3.5
        """
        self._execute(["data4.csv", "burger"], "2 , 3.5", "data4")

    def test_data5(self):
        """
        # direct match for combo
        $ python best-price.py data5.csv burger tofu_log
        2 , 7.0
        """
        self._execute(["data5.csv", "burger", "tofu_log"], "2 , 7.0", "data5")

    def test_data6_1(self):
        """
        # combo present, but no match
        $ python best-price.py data6.csv burger tofu_log
        2 , 8.0
        """
        self._execute(["data6.csv", "burger", "tofu_log"], "2 , 8.0", "data6_1")

    def test_data6_2(self):
        """
        # Two of the same menu items.
        $ python best-price.py data6.csv burger burger
        2 , 6.0
        """
        self._execute(["data6.csv", "burger", "burger"], "2 , 6.0", "data6_2")

    def test_data7(self):
        """
        # combo pack two of the same item
        $ python best-price.py data7.csv burger burger
        2 , 5.0
        """
        self._execute(["data7.csv", "burger", "burger"], "2 , 5.0", "data7")

    def test_data8(self):
        """
        # Many items
        $ python best-price.py data8.csv burger burger burger burger burger coffee macaroni pizza
        2 , 26.0
        """
        self._execute(["data8.csv"] + "burger burger burger burger burger coffee macaroni pizza".split(), "2 , 26.0", "data8")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRestaurant)
    unittest.TextTestRunner(verbosity=3).run(suite)
