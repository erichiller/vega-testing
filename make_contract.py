import datetime
import random
from mypy_extensions import TypedDict
from typing import List
import json

DAYS = 400
START = datetime.datetime.now()
MAX = 200


class DayRecord(TypedDict):
    """ Container for days trading """

    date: datetime.date
    open: float
    close: float
    high: float
    low: float
    volume: float
    symbol: str


records: List[DayRecord] = []

for i in range(int(START.timestamp()), int(START.timestamp()) + (30 * 86400), 86400):
    base = 0
    vals: List[float] = []
    for _ in range(4):
        vals.append( random.randrange(base * 100, MAX * 100) / 100 )
        base = int(vals[len(vals) - 1])
        # print(f"base={base}")
    # print(vals)
    # exit()
    _low, _open , _close, _high = vals
    if random.randint(0, 1):
        _open = vals[2]
        _close = vals[1]
    records.append( DayRecord(
        date=datetime.date.fromtimestamp(i),
        open=_open,
        close=_close,
        high=_high,
        low=_low,
        volume=random.randint(0, 500000),
        symbol="ZCN9"
    ) )


def dateformatter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


with open('out.json', 'w') as f:
    json.dump(records , f, default=dateformatter , indent=2 )

