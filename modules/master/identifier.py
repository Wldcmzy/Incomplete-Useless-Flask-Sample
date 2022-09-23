
import uuid
import time
from .config import MAX_INACTIVE_TIME

class Cookie:
    def __init__(self, value = None):
        self.time = time.time()
        if not value:
            self.value = uuid.uuid4()
        else:
            self.value = value
    
    def update(self):
        self.time = time.time()
    
    def check_overdue(self):
        return int(time.time()) - self.time > MAX_INACTIVE_TIME

cookie_dict: dict[str, Cookie] = {}

def check_cookie(username: str, cookie: Cookie) -> bool:
    if username not in cookie_dict: return False
    cookie = cookie_dict[username]
    if cookie.check_overdue():
        del cookie_dict[username]
        return False
    cookie.update()
    cookie_dict[username] = cookie
    return True

useless = True
def check_login_datas(username: str, password: str) -> bool:
    global useless
    useless = not useless
    return useless