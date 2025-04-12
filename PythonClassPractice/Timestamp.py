from __future__ import annotations

class Timestamp:
    """ Time and message for a timestamp. """

    def __init__(self, h: int, m: int, s: int, msg: str) -> None:
        """Initialize the hour h, minute m, second s, and message
        msg associated with this Timestamp.

        Precondition:
          - 0 <= h <= 23
          - 0 <= m <= 59
          - 0 <= s <= 59

        >>> ts1 = Timestamp(14, 10, 42, 'Relax')
        >>> ts1.hour
        14
        >>> ts1.min
        10
        >>> ts1.sec
        42
        >>> ts1.msg
        'Relax'
        """
        self.hour = h
        self.min = m
        self.second = s
        self.msg = msg

    def time(self) -> str:
        """Return a string representation of the time associated
        with this Timestamp.

        >>> ts1 = Timestamp(14, 9, 1, 'Relax')
        >>> ts1.time()
        '14:9:1'
        """
        return f'{self.hour}:{self.min}:{self.second}'

    def __eq__(self, other: Timestamp) -> bool:
        """Return True if and only if this Timestamp and the other
        Timestamp refer to the same time and have the same message.

        >>> ts1 = Timestamp(14, 10, 0, 'Relax')
        >>> ts2 = Timestamp(14, 10, 0, 'Panic')
        >>> ts3 = Timestamp(14, 10, 0, 'Relax')
        >>> ts4 = Timestamp(14, 14, 14, 'Write')
        >>> ts1 == ts2
        False
        >>> ts1 == ts3
        True
        >>> ts1 == ts4
        False
        """
        return self.time() == other.time() and self.msg == other.msg


class AlarmSchedule:
    """ Contains information about Timestamp objects in an alarm schedule. """

    def __init__(self) -> None:
        """Initialize an AlarmSchedule with an empty list named schedule.

        >>> alarms = AlarmSchedule()
        >>> alarms.schedule
        []
        """
        self.schedule = []

    def add(self, tstamp: Timestamp) -> None:
        """Modify schedule to add Timestamp tstamp, provided there is not
        an existing Timestamp with the same time.

        >>> alarms = AlarmSchedule()
        >>> alarms.add(Timestamp(14, 10, 42, 'Relax'))
        >>> alarms.add(Timestamp(14, 23, 39, 'Sigh'))
        >>> alarms.add(Timestamp(14, 10, 42, 'Burp'))
        >>> alarms.schedule[0].msg
        'Relax'
        >>> alarms.schedule[1].msg
        'Sigh'
        >>> len(alarms.schedule)
        2
        """
        for stamp in self.schedule:
            if stamp.time() == tstamp.time():
                return

        self.schedule.append(tstamp)

