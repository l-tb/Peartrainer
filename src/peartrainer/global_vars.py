"""Supply global variables for Peartrainer."""

intervals = [
    "u",
    "2b",
    "2",
    "3b",
    "3",
    "4",
    "5b",
    "5",
    "6b",
    "6",
    "7b",
    "7",
    "8",
]

intervalNames = {
    "u": "unison",
    "2b": "minor second",
    "2": "major second",
    "3b": "minor third",
    "3": "major third",
    "4": "perfect fourth",
    "5b": "tritone",
    "5": "perfect fifth",
    "6b": "minor sixth",
    "6": "major sixth",
    "7b": "minor seventh",
    "7": "major seventh",
    "8": "octave",
}

helpStr = f"""
Interval Keys:
{intervalNames[intervals[0]]}: {intervals[0]}
{intervalNames[intervals[1]]}: {intervals[1]}
{intervalNames[intervals[2]]}: {intervals[2]}
{intervalNames[intervals[3]]}: {intervals[3]}
{intervalNames[intervals[4]]}: {intervals[4]}
{intervalNames[intervals[5]]}: {intervals[5]}
{intervalNames[intervals[6]]}: {intervals[6]}
{intervalNames[intervals[7]]}: {intervals[7]}
{intervalNames[intervals[8]]}: {intervals[8]}
{intervalNames[intervals[9]]}: {intervals[9]}
{intervalNames[intervals[10]]}: {intervals[10]}
{intervalNames[intervals[11]]}: {intervals[11]}
{intervalNames[intervals[12]]}: {intervals[12]}

If you don't know the answere type 'skip' to reveal the interval
and get a new question.

To exit Peartrainer type 'quit' and 'leave' to return to the main menu.
"""
