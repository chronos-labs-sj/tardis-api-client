#!/usr/bin/env python3

# pip install tardis-dev
# requires Python >=3.6
from tardis_dev import datasets

datasets.download(
    exchange="binance-futures",
    data_types=[
        "incremental_book_L2",
        "trades",
        "quotes",
        # "derivative_ticker",
        "book_snapshot_25",
        # "liquidations",
        "book_ticker"
    ],
    from_date="2022-08-29",
    to_date="2022-09-11",
    symbols=["ETHUSDT"],
    api_key="TD.rOrO1TMLcT14JL8t.ZbIWkbhZBscleUe.eLg6DErArfzvqt2.fbCzMy0Ra9eA6sj.QAONcTjlSOfwYNQ.4Be7",
)