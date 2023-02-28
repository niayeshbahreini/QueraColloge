class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    out = []
    for x in func_ls:
        try:
            x()
            a = ExceptionProxy("ok!", x)
        except Exception as e:
            print(e)
            a = ExceptionProxy(str(e), x)
        out.append(a)
    return out


def f():
    1 / 0


def g():
    pass


tr_ls = transform_exceptions([f, g])

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)