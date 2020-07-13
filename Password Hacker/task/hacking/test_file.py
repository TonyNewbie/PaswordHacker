from datetime import datetime
import time

dictionary = {}
start = datetime.now()
time.sleep(3)
dictionary['firstTime'] = datetime.now() - start
start = datetime.now()
time.sleep(6)
dictionary['secondTime'] = datetime.now() - start
print(dictionary)
print(type(max(dictionary)))
