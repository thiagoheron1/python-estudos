
# Levels: debug, info, warning, error and critical, can create additional levels
# 0 - NOTSET
# 10 - DEBUG
# 20 - INFO
# 30 - WARNING
# 40 - ERROR
# 50 - CRITICAL


import logging

# Create and Configure logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'

logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w' # change append to writer
                    #filename = './logging/script.log',
                    )
logger = logging.getLogger('TheLoggerName')



import math
def quadratic_formula(a, b, c):
    '''Return the solutions to the equation ax^ + bx + c = 0.'''
    logger.info('quatric_formula({0}, {1}, {2})'.format(a, b, c))

    # Compute the discrimant
    logger.debug('# Compute the discriminant')
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug('# Compute the two roots')
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    
    # Return the two roots
    logger.debug('# Return the roots')
    return(root1, root2)

roots = quadratic_formula(1, 0, -4)
#roots = quadratic_formula(1, 0, 1)

logger.info(f'Result: {roots}')