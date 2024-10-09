# -*- coding: utf-8 -*-
import unittest

from gilded_rose import gilded_rose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [gilded_rose.Item("foo", 0, 0)]
        gilded_rose = gilded_rose.GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
