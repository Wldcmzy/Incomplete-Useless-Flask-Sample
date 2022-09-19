import os
from pathlib import Path
import threading

TIMESPAN_SDW = 60 * 5

def run_SDW():
    path = Path(__file__).parent / "modules" / "SDW" / "process.py"
    os.system(f'python {str(path)}')
    t = threading.Timer(TIMESPAN_SDW, run_SDW)
    t.start()

# def run_something():
#     pass

def run_processes_win():
    run_SDW()
    # run_something()