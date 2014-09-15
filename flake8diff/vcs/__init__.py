from __future__ import unicode_literals, print_function
import inspect

from .base import VCSBase
from .git import GitVCS  # noqa


SUPPORTED_VCS = dict(
    (value.name, value)
    for value in filter(lambda i: (i is not VCSBase
                                   and inspect.isclass(i)
                                   and issubclass(i, VCSBase)),
                        locals().values())
)
