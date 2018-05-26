import pathlib
import numpy as np

def foo(x):
  return np.mean(x)


if __name__ == "__main__":
  x = foo([1,2])
  p = pathlib.Path(".")