 
import hashlib
import time
import datetime
import random 
def find_gold(): 
  x = 0 
  y = 0
  fh=open("hash-basic.txt","r")
  data1 = fh.read()
  print("char length = ", len(data1))
  Diffcult_number = str(input('Degree of dificulty(exmple:000 ; 0000 ; 00000):'))
  Begin_time = datetime.datetime.now()
  print('time of begin',Begin_time)
  while True:
    combine_string=""
    x += 1  
    string = data1 

    
    combine_string = string + str(x)
    h = hashlib.sha256()                    # sha256 
    h.update(combine_string.encode('utf-8'))# utf-8 
    gold_hash = h.hexdigest()
    #print(gold_hash)
    #startTime = time.perf_counter()
    if gold_hash[0:len(Diffcult_number)] == Diffcult_number: #compare

      End_time = datetime.datetime.now()
      print('time of end',End_time)
      print('power :{}'.format(x), 'seconds-consuming',(End_time -Begin_time).seconds )
      #print("string:",combine_string)
      print('hash:%s' % gold_hash)
      print('success！total',x,'time ' )
      break
    elif gold_hash[0:len(Diffcult_number)] != Diffcult_number:#compare
            
      End_time = datetime.datetime.now()
      if ( (End_time -Begin_time).seconds == 10):
        print(End_time, 'power = {}  '.format(x-y),'total',x/1000/1000,'M-time')
        Begin_time = datetime.datetime.now()
        y=x
      continue
  
if __name__ == '__main__':#main
  find_gold()
