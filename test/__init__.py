import enum
import sys
from io import StringIO
from typing import Any, Callable, Optional

import noarg


MANUAL = True


def get_and_clear_io(iobuf: StringIO):
    result = iobuf.getvalue()
    iobuf.truncate(0)
    iobuf.seek(0)
    return result


def run_cli_and_manual(
    iobuf: StringIO,
    func: Callable,
    argv: list[str],
    args: list[Any],
    kwargs: Optional[dict[str, Any]] = None,
    noarg_kwargs: Optional[dict[str, Any]] = None,
):
    if noarg_kwargs is None:
        noarg_kwargs = dict()

    func(*args, **kwargs)
    manual = get_and_clear_io(iobuf)

    sys.argv.extend(argv)
    noarg.run(output=iobuf, **noarg_kwargs)
    cli = get_and_clear_io(iobuf)

    return cli, manual


class Permissions(enum.Flag):
    """
    Permission flags

    :var READ: [-r] allows for reads
    :var WRITE: [-w] allows for writes
    :var EXECUTE: [-x] allows for execution
    """

    READ = 4
    WRITE = 2
    EXECUTE = 1


class PermissionsAlt(enum.Flag):
    """
    Permission flags
    """

    READ = 4
    """[-r] allows for reads"""

    WRITE = 2
    """[-w] allows for writes"""

    EXECUTE = 1
    """[-x] allows for execution"""


class HiBye(enum.Enum):
    HI = "Hi!"
    BYE = "Bye!"
