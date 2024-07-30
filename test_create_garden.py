import unittest
from main import create_garden, counting_items, plant, day_increment, grow_garden


class Garden(unittest.TestCase):
    def setUp(self):
        self.garden1 = [
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", "F"],
            ["F", ".", "W", ".", ".", "W", ".", ".", "F"],
            [".", "W", ".", ".", ".", ".", ".", "W", "."],
            [".", "F", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "F", ".", ".", ".", ".", ".", ".", "F"],
            [".", ".", "F", ".", ".", "W", "F", ".", "F"],
            [".", ".", "W", ".", ".", "W", ".", ".", "."],
        ]
        self.garden2 = [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]

        # Number of flowers (F): 0
        # Number of weeds (W): 0

        self.garden3 = [
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
            ["F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ]
        # Number of flowers (F): 63
        # Number of weeds (W): 0

        self.garden4 = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        # Number of flowers (F): 0
        # Number of weeds (W): 63

        self.garden5 = [
            ["f", ".", ".", ".", ".", ".", ".", "w", "."],
            [".", ".", ".", ".", "w", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "f", ".", "."],
            [".", "f", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "w", "."],
            [".", ".", ".", "f", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "w", ".", ".", "."],
        ]

    def test_create_func(self):
        test_case_1 = [-1, -1]
        test_case_2 = [100, 100]
        test_case_3 = [7, 7]
        test_case_4 = [2.25, 3.456]

        self.assertRaises(ValueError, create_garden, test_case_1[0], test_case_1[1])
        self.assertEqual(len(create_garden(test_case_2[0], test_case_2[1])), 100)
        self.assertEqual(len(create_garden(test_case_3[0], test_case_3[1])), 7)
        self.assertRaises(ValueError, create_garden, test_case_4[0], test_case_4[1])

    def test_counting_items(self):
        self.assertEqual(counting_items(self.garden1, 7, 9), (8, 8))
        self.assertEqual(counting_items(self.garden2, 7, 9), (0, 0))
        self.assertEqual(counting_items(self.garden3, 7, 9), (63, 0))
        self.assertEqual(counting_items(self.garden4, 7, 9), (0, 63))
        self.assertEqual(counting_items(self.garden5, 7, 9), (0, 0))

    def test_plant(self):
        self.assertTrue(
            plant(self.garden1, 5, 4, "F")
        )  # this is to test for valid condition flowers
        self.assertTrue(plant(self.garden1, 3, 6, "W"))  # test for weeds
        self.assertRaises(
            ValueError, plant, self.garden1, 3, 4, "M"
        )  # test for if invalid item returns error
        self.assertRaises(
            IndexError, plant, self.garden2, 300, 200, "F"
        )  # test for out of range error
        self.assertFalse(
            plant(self.garden3, 2, 2, "F")
        )  # since garden 3 is full of flowers ,test if it returns false if the garden is full
        self.assertFalse(plant(self.garden4, 2, 4, "W"))  # same test for weeds

    def test_day_inc(self):

        garden_after_day = [
            ["W", "W", ".", ".", ".", ".", "W", "F", "F"],
            ["F", "F", "W", "W", "W", "F", "W", "F", "F"],
            [".", "W", ".", "W", ".", ".", "W", ".", "W"],
            [".", "F", "F", ".", ".", ".", ".", ".", "."],
            [".", "F", ".", ".", ".", ".", ".", ".", "F"],
            [".", "F", "F", "W", "W", "W", "F", "F", "F"],
            [".", "W", "W", ".", ".", "W", ".", ".", "."],
        ]

        self.assertListEqual(day_increment(self.garden1, 7, 9), garden_after_day)


if __name__ == "__main__":
    unittest.main(verbosity=2)
