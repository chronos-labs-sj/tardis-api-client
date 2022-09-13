#!/usr/bin/env python3

# pip install tardis-dev
# requires Python >=3.6
from tardis_dev import datasets
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import shlex

def parse_args():
    default_data_types="incremental_book_L2",
            "trades",
            "quotes",
            "book_snapshot_25",
            "book_ticker"

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, conflict_handler='resolve')
    parser.add_argument('--exchange', '-ex', default='binance', help="the exchange to pull data from")
    parser.add_argument('--from_date', '-from', help='from date - inclusive', required=True)
    parser.add_argument('--to_date', '-to', help='to date - exclusive', required=True)
    parser.add_argument('--symbols', '-sym', default='BTCUSDT', help="whitespace separated list of symbols")
    parser.add_argument('--data-types', '-dt', default=default_data_types, help='data types to be included in the datasets')

    args = parser.parse_args()
    return args


def download(args):
    datasets.download(
        # exchange="binance-futures",
        exchange=args.exchange,
        data_types=[
            "incremental_book_L2",
            "trades",
            "quotes",
            # "derivative_ticker",
            "book_snapshot_25",
            # "liquidations",
            "book_ticker"
        ],
        from_date=args.from_date,
        to_date=args.to_date,
        symbols=shlex.split(args.symbols),
        api_key="TD.rOrO1TMLcT14JL8t.ZbIWkbhZBscleUe.eLg6DErArfzvqt2.fbCzMy0Ra9eA6sj.QAONcTjlSOfwYNQ.4Be7",
    )

def main():
    args = parse_args()
    download(parse_args())

if __name__ == "__main__":
    main()