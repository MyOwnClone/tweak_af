import inspect
import dis


def cid():
    f = inspect.currentframe().f_back
    #dis.dis(f.f_code)
    caller_id = (f.f_lineno, f.f_lasti)
    return caller_id


print((cid(), cid(), cid(), cid(), cid()))
print((cid(), cid(), cid(), cid(), cid()))
