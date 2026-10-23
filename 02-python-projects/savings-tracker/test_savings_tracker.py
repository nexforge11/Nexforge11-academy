# Tests for savings_tracker.py
# Run them with:  python -m unittest test_savings_tracker.py

import os
import tempfile
import unittest

import savings_tracker as st


class SavingsTrackerTests(unittest.TestCase):

    def setUp(self):
        self.tracker = st.new_tracker(100)

    def test_new_tracker_starts_empty(self):
        self.assertEqual(st.balance(self.tracker), 0)
        self.assertEqual(st.remaining(self.tracker), 100)

    def test_goal_must_be_positive(self):
        with self.assertRaises(ValueError):
            st.new_tracker(0)

    def test_lesson_01_example(self):
        # Same numbers as the Lesson 01 mini project.
        st.add_transaction(self.tracker, 75)
        self.assertEqual(st.remaining(self.tracker), 25)
        st.add_transaction(self.tracker, 10)
        self.assertEqual(st.balance(self.tracker), 85)
        self.assertEqual(st.remaining(self.tracker), 15)

    def test_withdrawal_reduces_balance(self):
        st.add_transaction(self.tracker, 50)
        st.add_transaction(self.tracker, -20, "bus pass")
        self.assertEqual(st.balance(self.tracker), 30)

    def test_cannot_withdraw_more_than_saved(self):
        st.add_transaction(self.tracker, 10)
        with self.assertRaises(ValueError):
            st.add_transaction(self.tracker, -11)
        self.assertEqual(st.balance(self.tracker), 10)

    def test_zero_amount_rejected(self):
        with self.assertRaises(ValueError):
            st.add_transaction(self.tracker, 0)

    def test_progress_is_capped_when_goal_passed(self):
        st.add_transaction(self.tracker, 150)
        self.assertEqual(st.remaining(self.tracker), 0)
        self.assertEqual(st.progress_percent(self.tracker), 100)
        self.assertEqual(st.progress_bar(self.tracker, width=10), "[##########]")

    def test_progress_bar_half_way(self):
        st.add_transaction(self.tracker, 50)
        self.assertEqual(st.progress_percent(self.tracker), 50)
        self.assertEqual(st.progress_bar(self.tracker, width=10), "[#####-----]")

    def test_save_and_load_round_trip(self):
        st.add_transaction(self.tracker, 40, "birthday money", when="2026-10-01")
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            st.save(self.tracker, path)
            self.assertEqual(st.load(path), self.tracker)

    def test_load_missing_file_returns_none(self):
        self.assertIsNone(st.load("does-not-exist.json"))


if __name__ == "__main__":
    unittest.main()
