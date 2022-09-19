from SDW_main import SDW_draw
import time
import sys

SDW_countZ = 0

def run():
    global SDW_countZ
    SDW_countZ += 1
    print(f'execute {SDW_countZ} times', time.localtime()[ : 6])
    SDW_draw()
    sys.exit()

if __name__ == '__main__':
    run()
    
