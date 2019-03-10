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

    date: str   # iso
    open: float
    close: float
    high: float
    low: float
    volume: float
    symbol: str


print(f"starting at timestamp {START.timestamp()} ( {START} )")


records: List[DayRecord] = []

for date in range(int(START.timestamp()), int(START.timestamp()) + (DAYS * 86400), 86400):
    base = 0
    vals: List[float] = []
    for i in range(4):
        vals.append( random.randrange(int(base) * 100, ( (MAX - ((4 - i) * 10)) * 100)) / 100 )
        base = int(vals[len(vals) - 1])
        # print(f"base={base}")
    # print(vals)
    # exit()
    _low, _open , _close, _high = vals
    if random.randint(0, 1):
        _open = vals[2]
        _close = vals[1]
    records.append( DayRecord(
        date=datetime.date.fromtimestamp(date).isoformat(),
        open=_open,
        close=_close,
        high=_high,
        low=_low,
        volume=random.randint(0, 500000),
        symbol="ZCN9"
    ) )



# def dateformatter(o: datetime.date):
#     if isinstance(o, (datetime.date)):
#         print(f"{o} -> returning {o.isoformat()}")
#         return o.isoformat()
#     print("NOT FOUND.")


with open('out.json', 'w', newline="\n") as f:
    json.dump(records , f , indent=2 )

