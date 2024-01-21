class ProgressBar:
  def __init__(self, n):
    self.n = n
    self.c = 0
    self.p = 0

  def tick(self):
    self.c = self.c + 1
    p = self.c * 100 // self.n
    if p > self.p:
      print("\r[" + ('.' * p) + (' ' * (100-p)) + ']', end="")
      self.p = p
    if self.c == self.n:
      print("")
