from SDW_main import SDW_draw
import time
import sys

def run():
    print(f'execute once', time.localtime()[ : 6])
    SDW_draw()
    sys.exit()

if __name__ == '__main__':
    run()
    
