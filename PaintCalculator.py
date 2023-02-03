import unittest

"""Calculates the floor area and amount of paint needed usingthe parameters
Length
Width
Height
Paint Coverage
and using unittest to make sure there were no errors when run."""


def calculate_paint_needed(length, width, height, paint_coverage):
    # Calculate the area of the floor in meteres
    floor_area = length * width
    # Calculate the volume of the room
    volume = length * width * height
    # Calculate the amount of paint required
    paint_needed = int(volume / paint_coverage)
    return floor_area, paint_needed


class PaintCalculatorTest(unittest.TestCase):
    def test_calculate_paint_needed(self):
        # Test case 1
        length = 5
        width = 4
        height = 3
        paint_coverage = 10
        expected_floor_area = 20
        expected_paint_needed = 6
        result = calculate_paint_needed(length, width, height, paint_coverage)
        self.assertEqual(result, (expected_floor_area, expected_paint_needed))

        # Test case 2
        length = 10
        width = 8
        height = 6
        paint_coverage = 10
        expected_floor_area = 80
        expected_paint_needed = 48
        result = calculate_paint_needed(length, width, height, paint_coverage)
        self.assertEqual(result, (expected_floor_area, expected_paint_needed))


if __name__ == '__main__':
    unittest.main()
