import time, logging
from datetime import datetime

a = 0
while 1:
    now = datetime.now()
    a += 1
        
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.basicConfig(filename='app.log', filemode='a', level= logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # print(date_time)
    logging.info(a)
    time.sleep(1)