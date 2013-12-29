def hasmethod(obj, method_name):
  return hasattr(obj, method_name) and callable(getattr(obj, method_name))

def log(fn):
  def logger(*t, **d):
    if hasmethod(t[0], fn.__name__):
      args = t[1:]
      prefix = t[0].__class__.__name__ + "." + fn.__name__
    else:
      args = t[:]
      prefix = fn.__name__
    str_args = ", ".join(str(arg) for arg in args)
    str_kwargs = ", ".join(str(k) + '=' + str(v) for k, v in d.items())
    join = ""
    if str_args and str_kwargs:
      join = ", "
    result = fn(*t, **d)
    print prefix + "(" + str_args + join + str_kwargs + ') ->',
    print str(result)
    return result
  return logger


if __name__ == '__main__':

  @log
  def add(x, y):
    return x + y

  class Adder:
    @log
    def add(self, x, y):
      return x + y

  add(3, 5)
  add(1, y=2)

  adder = Adder()
  adder.add(1, 2)


