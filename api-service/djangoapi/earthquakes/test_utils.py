import unittest
from datetime import datetime, timedelta

from earthquakes.utils import create_capture_ranges


class TestCaptureRanges(unittest.TestCase):
    def test_empty_input_returns_empty_result(self):
        self.assertEqual(create_capture_ranges([]), [])

    def test_single_date_should_return_single_range(self):
        dates = [datetime(2021, 8, 24)]
        expected = [(datetime(2021, 8, 24), datetime(2021, 8, 24))]
        self.assertEqual(create_capture_ranges(dates), expected)

    def test_two_dates_within_the_max_gap(self):
        dates = [datetime(2021, 8, 24), datetime(2021, 8, 15)]
        expected = [(datetime(2021, 8, 15), datetime(2021, 8, 24))]
        self.assertEqual(create_capture_ranges(dates), expected)

    def test_multiple_dates_within_the_max_gap(self):
        dates = [
            datetime(2021, 8, 2),
            datetime(2021, 8, 7),
            datetime(2021, 8, 15),
            datetime(2021, 8, 28)
        ]
        expected = [(datetime(2021, 8, 2), datetime(2021, 8, 28))]
        self.assertEqual(create_capture_ranges(dates), expected)

    def test_some_dates_beyond_the_max_gap(self):
        dates = [
            datetime(2021, 7, 2),
            datetime(2021, 8, 7),
            datetime(2021, 8, 15),
            datetime(2021, 8, 28)
        ]
        expected = [
            (datetime(2021, 7, 2), datetime(2021, 7, 2)),
            (datetime(2021, 8, 7), datetime(2021, 8, 28)),
        ]
        self.assertEqual(create_capture_ranges(dates), expected)

    def test_multiple_dates_beyond_the_max_gap(self):
        dates = [
            datetime(2021, 2, 2),
            datetime(2021, 5, 7),
            datetime(2021, 8, 15),
            datetime(2021, 12, 25)
        ]
        expected = [
            (datetime(2021, 2, 2), datetime(2021, 2, 2)),
            (datetime(2021, 5, 7), datetime(2021, 5, 7)),
            (datetime(2021, 8, 15), datetime(2021, 8, 15)),
            (datetime(2021, 12, 25), datetime(2021, 12, 25)),
        ]
        self.assertEqual(create_capture_ranges(dates), expected)

    def test_three_full_groups(self):
        start_date = datetime(2000, 1, 1)
        dates = [start_date + timedelta(days=x) for x in range(30)]
        ranges = create_capture_ranges(dates, max_gap=10)
        self.assertEqual(ranges[0][0], datetime(2000, 1, 1))
        self.assertEqual(ranges[0][1], datetime(2000, 1, 10))
        self.assertEqual(ranges[1][0], datetime(2000, 1, 11))
        self.assertEqual(ranges[1][1], datetime(2000, 1, 20))
        self.assertEqual(ranges[2][0], datetime(2000, 1, 21))
        self.assertEqual(ranges[2][1], datetime(2000, 1, 30))

    def test_always_between_max_gap(self):
        def get_range_gap(date_range):
            start, end = date_range
            return (end - start).days + 1
        start_date = datetime(2000, 1, 1)
        dates = [start_date + timedelta(days=x) for x in range(600)]

        ranges = create_capture_ranges(dates, max_gap=1)
        self.assertTrue(all(get_range_gap(r) == 1 for r in ranges))

        ranges = create_capture_ranges(dates, max_gap=7)
        self.assertTrue(all(0 < get_range_gap(r) <= 7 for r in ranges))

        ranges = create_capture_ranges(dates, max_gap=45)
        self.assertTrue(all(0 < get_range_gap(r) <= 45 for r in ranges))


if __name__ == '__main__':
    unittest.main()
