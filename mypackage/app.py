import pathlib
import numpy as np

def foo(x):
  return np.mean(x)

def foo_from_file(filename):
  x = np.fromfile(filename, sep=" ")
  return np.mean(x)
    

if __name__ == "__main__":
  x = foo([1,2])
  p = pathlib.Path(".")