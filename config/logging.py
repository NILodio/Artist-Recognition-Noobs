
import os
import logging


def create_log(log_name, special_formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')):
    """
    Create a log file with the given name and return the logger object.
    
    :param log_name: The name of the log file.
    
    """
    logging_manager = logging.Logger.manager
    if log_name not in logging_manager.loggerDict:
        logfile = os.path.join('logs', '%s.log' % log_name)
        
        try:
            if not os.path.exists(logfile):
                open(logfile, 'w').close()
                os.chmod(logfile, 0o664)
        except IOError:
            pass
        logger = logging.getLogger(log_name)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(logfile) 
        handler.setFormatter(special_formatter)
        logger.addHandler(handler)
    return logging_manager.loggerDict[log_name]


