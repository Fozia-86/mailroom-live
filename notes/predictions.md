# My predictions

Write every guess here BEFORE running any code. A guess made after the output is not a guess.

## Step 0: The base

- Newsletter name: Kettlebird Tea's Steep Club
- Audience: Tea lovers and subscribers who want updates on new tea blends, monthly boxes, and club news.

## Step 1: Count your subscribers

- Total subscribers: 24
- daily-drinkers: 8
- gift-buyers: 8
- tea-curious: 8
- Modify task: subscribers who gave consent: 24 (all 24 rows have "waitlist form" in the consent column)

## Step 2 (13.9 Dates) — Run date: 2026-11-20
- Subscribers joined in the last 30 days: 7
- Does 2026-10-21 count? Yes, because 2026-11-20 minus 30 days is 2026-10-21 (inclusive boundary).
- Next send date (first Monday of the next month): 2026-12-07
- The send after that (first Monday of January 2027): 2027-01-04
- Does a join on 2026-10-20 count? No, because 2026-10-20 is 31 days before 2026-11-20, so it falls outside the last 30 days (which start on 2026-10-21).
- Does a join after the run date (such as 2026-11-25) count? No, because it is after 2026-11-20 and will only count in a future run.

## Step 3: The 30th of February
1. **Will Mailroom crash?** Yes, it will crash with an unhandled error because `2026-02-30` is not a valid calendar date.
2. **What will the last line of the error say?** `ValueError: day is out of range for month` (or `ValueError: Invalid isoformat string: '2026-02-30'`).
3. **Which of your functions will it name?** It will name the function in `mailroom.py` that reads and parses the subscriber dates (such as `count_recent_subscribers` or `parse_date`).

### Step 3: what actually happened (my readings)

**Error 1: bad date 2026-02-30 in data/subscribers.csv (Jonas Berg)**
- My reading: "day 30 ko aik range me hona chiey mean date ka format theek ho, joined countt ka function call huwa hai previous line se error aya hai, value ko theek se nhi dia gia or format theek nhi hai"
- Actual: `ValueError: day 30 must be in range 1..28 for month 2 in year 2026`, mailroom.py line 51 in count_joined_since (called from line 118).
- One sentence: mailroom.py line 51 in count_joined_since crashed with ValueError because data/subscribers.csv line 25 had 2026-02-30, a day that doesn't exist.
- Fix: the data, not the code (git restore data/subscribers.csv). Line 51 was given the wrong value; it didn't make it.

**Modify: renamed the column joined_on -> joined (in a temporary copy outside the project)**
- My reading: "iso format invalid, type value missing, count joined function call line 51 error"
- Actual: `ValueError: Invalid isoformat string: 'joined'`, line 51 in count_joined_since (called from line 118).
- One sentence: line 51 crashed because the header was renamed to `joined`, so line 50 (which skips the header only when it says "joined_on") didn't skip it, and the word 'joined' was read as a date.
- Lesson: read the traceback bottom-up; ask "did this line make the bad value, or was it given it?"
