# Why logger file?
# Function is going to excute and wanted to log that
import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # at which time I have executed my pipeline
log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
) 
