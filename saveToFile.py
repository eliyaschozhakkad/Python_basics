import os
import logging

#logging.basicConfig(filename = 'saveToFile.log', level = logger.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

fh=logging.FileHandler('saveTofile.log')
fh.setFormatter(f)

logger.addHandler(fh)

def namecheck(name):
    logger.debug(f"Checking name {name}")
    if os.path.exists('data.txt'):
        with open('data.txt','r') as readFile:
            for line in readFile:
                if line.lower().startswith(f'name:{name.lower()}'):
                    logger.error(f'Name:{name} already exists')
                    return False
            if len(name)  == 0:
                logger.critical('Name cannot be blank')
                return False
            elif not name.isalpha():
                logger.critical('name must be alphabet')
                return False
            else:
                logger.error('Check successfull')
                return True
    else:
        logger.debug('No data found')
        return True

def saveData(name, age ,email):
    logger.debug(f'Saving details of {name}')
    with open('data.txt','a') as appendFile:
        appendFile.write(f'Name:{name} - Age:{age} - Email:{email}\n')
        print('Details saved successfully')

logger.info('End of saveToFile Program')
logger.debug('#######################')