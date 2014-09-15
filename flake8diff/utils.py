from __future__ import unicode_literals, print_function
import logging
import subprocess


def _get_logger(level=None):
    """
    Get logger with specified level
    """
    if level is None:
        level = logging.ERROR

    logger = logging.getLogger('flake8diff')
    FORMAT = "%(asctime)-15s %(name)s %(levelname)s %(message)s"
    logging.basicConfig(format=FORMAT)
    logger.setLevel(level)

    return logger


def _execute(cmd, logger=None, strict=False):
    """
    Make executing a command locally a little less painful
    """
    if logger is None:
        logger = _get_logger()

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

    return out
