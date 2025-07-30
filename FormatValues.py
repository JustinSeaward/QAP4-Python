# Library of functions for formatting numbers and dates.

import datetime
import sys

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

### New Functions ###

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
