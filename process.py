import os
from pathlib import Path
import threading

TIMESPAN_SDW = 60 * 5

def run_SDW(cmd):
    path = Path(__file__).parent / "modules" / "SDW" / "process.py"
    def _(cmd, path):
        os.system(f'{cmd} {str(path)}')
        t = threading.Timer(TIMESPAN_SDW, _, args=[cmd, path])
        t.start()
    t = threading.Timer(0, _, args=[cmd, path])
    t.start()

# def run_something():
#     pass

def run_processes_win():
    run_SDW('python')
    # run_something()

def run_processes_linux():
    run_SDW('python3')

# if __name__ == '__main__':
#     run_processes_win()