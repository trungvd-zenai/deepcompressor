# Python 3.10 compat: typing.Self was added in 3.11
import typing as _typing

if not hasattr(_typing, "Self"):
    from typing_extensions import Self as _Self

    _typing.Self = _Self

from .version import __version__  # noqa: F401
