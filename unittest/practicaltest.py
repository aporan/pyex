import unittest

import datetime
## Actual Code

class DatePattern(object):

    def __init__(self, year, month, day, weekday=0):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    def matches(self, date):
        return (self.yearMatches(date) and
                self.monthMatches(date) and
                self.dayMatches(date) and
                self.weekdayMatches(date))

    def yearMatches(self, date):
        if not self.year: return True
        return self.year == date.year

    def monthMatches(self, date):
        if not self.month: return True
        return self.month == date.month

    def dayMatches(self, date):
        if not self.day: return True
        return self.day == date.day

    def weekdayMatches(self, date):
        if not self.weekday: return True
        return self.weekday == date.weekday()

## Testing Code

class PracticalTest(unittest.TestCase):

    def test_date_pattern_matches(self):
        p = DatePattern(2018, 1, 12)
        d = datetime.date(2018, 1, 12)
        self.assertTrue(p.matches(d))

    def test_date_patten_does_not_match(self):
        p = DatePattern(2018, 1, 12)
        d = datetime.date(2018, 1, 11)
        self.assertFalse(p.matches(d))

    def test_date_year_wildcard(self):
         p = DatePattern(0, 1, 10)
         d = datetime.date(2018, 1, 10)
         self.assertTrue(p.matches(d))

    def test_date_month_wildcard(self):
         p = DatePattern(0, 0, 10)
         d = datetime.date(2018, 1, 10)
         self.assertTrue(p.matches(d))

    def test_date_day_wildcard(self):
         p = DatePattern(0, 0, 10)
         d = datetime.date(2018, 1, 10)
         self.assertTrue(p.matches(d))

    def test_matches_weekday(self):
        p = DatePattern(0, 0, 0, 2) # 2 is Wednesday
        d = datetime.date(2004, 9, 29)
        self.failUnless(p.matches(d))

if __name__=="__main__":
    unittest.main()
