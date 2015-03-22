from __future__ import unicode_literals, print_function
import logging
import subprocess


logger = logging.getLogger(__name__)


def _execute(cmd, strict=False):
    """
    Make executing a command locally a little less painful
    """
    logger.debug("executing {0}".format(cmd))
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate()
    return_code = process.wait()

    # flake8 by default returns non-zero
    # status code when any violations have been found
    # so only log if error message is present
    if return_code != 0 and (err or strict):
        logger.error(err)
        if strict:
            raise subprocess.CalledProcessError(return_code, cmd)

    return out.decode('utf-8')
