from datetime import datetime
import logging
import os

dir_path = 'logs'
filename = "{:%Y-%m-%d_%X}".format(datetime.now()) + '.log'

def create_logger(log_folder):

	logging.captureWarnings(True)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	my_logger = logging.getLogger('py.warnings')
	my_logger.setLevel(logging.INFO)

	os.makedirs(log_folder,exist_ok=True)


	fileHandler = logging.FileHandler(log_folder+'/'+filename, 'w', 'utf-8')
	fileHandler.setFormatter(formatter)
	my_logger.addHandler(fileHandler)



	consoleHandler = logging.StreamHandler()
	consoleHandler.setLevel(logging.DEBUG)
	consoleHandler.setFormatter(formatter)
	my_logger.addHandler(consoleHandler)
	return my_logger

logger = create_logger(dir_path)	