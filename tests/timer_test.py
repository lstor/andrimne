from andrimne.timer import *
import unittest


class TimerTest(unittest.TestCase):

    def test_smoketest(self):
        self.assertEqual('', prettify(0))
        self.assertEqual('one hour, one second', prettify(3601))
        self.assertEqual('one hour, two minutes, three seconds', prettify(62 * 60 + 3))
        self.assertEqual('15 hours, 15 minutes, 15 seconds', prettify(15 * 3600 + 15 * 60 + 15))

    def test_decimals(self):
        self.assertEqual('', prettify(0))
        self.assertEqual('0.001 seconds', prettify(0.001))
        self.assertEqual('0.200 seconds', prettify(0.2))
        self.assertEqual('0.999 seconds', prettify(0.999))
        self.assertEqual('one second', prettify(1))

    def test_named_numbers(self):
        self.assertEqual('', prettify(0))
        self.assertEqual('one second', prettify(1))
        self.assertEqual('two seconds', prettify(2))
        self.assertEqual('three seconds', prettify(3))
        self.assertEqual('four seconds', prettify(4))
        self.assertEqual('five seconds', prettify(5))
        self.assertEqual('six seconds', prettify(6))
        self.assertEqual('seven seconds', prettify(7))
        self.assertEqual('eight seconds', prettify(8))
        self.assertEqual('nine seconds', prettify(9))
        self.assertEqual('ten seconds', prettify(10))
        self.assertEqual('eleven seconds', prettify(11))
        self.assertEqual('twelve seconds', prettify(12))
        self.assertEqual('13 seconds', prettify(13))

    def test_minute(self):
        self.assertEqual('59 seconds', prettify(59))
        self.assertEqual('one minute', prettify(60))
        self.assertEqual('one minute, one second', prettify(61))
        self.assertEqual('one minute, two seconds', prettify(62))

    def test_hour(self):
        self.assertEqual('59 minutes', prettify(59 * 60))
        self.assertEqual('one hour', prettify(60 * 60))
        self.assertEqual('one hour, one minute', prettify(61 * 60))
        self.assertEqual('one hour, two minutes', prettify(62 * 60))


if __name__ == '__main__':
    unittest.main()
