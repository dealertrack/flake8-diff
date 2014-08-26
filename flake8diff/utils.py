from __future__ import unicode_literals, print_function
import logging
import subprocess


def _execute(cmd, logger):
    """
    Make executing a command locally a little less painful
    """
    logging.debug("executing {}".format(cmd))
    process = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate()
    return_code = process.wait()
    # flake8 by default returns non-zero
    # status code when any violations have been found
    # so only log if error message is present
    if return_code != 0 and err:
        logging.error(err)
    return out
