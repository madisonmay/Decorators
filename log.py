
def log(fn):
  def logger(*t, **d):
    str_args = ", ".join(str(arg) for arg in t)
    str_kwargs = ", ".join(str(k) + '=' + str(v) for k, v in d.items())
    join = ""
    if str_args and str_kwargs:
      join = ", "
    result = fn(*t, **d)
    print fn.__name__ + "(" + str_args + join + str_kwargs + ') ->',
    print str(result)
    return result
  return logger


if __name__ == '__main__':

  @log
  def add(x, y):
    return x + y

  add(3, 5)
  add(1, y=2)


