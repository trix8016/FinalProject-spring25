class HashTable:
  def __init__(self):
      self.table = {}

  def insert(self, key, value):
      self.table[key] = value

  def get(self, key):
      return self.table.get(key, None)

  def delete(self, key):
      if key in self.table:
          del self.table[key]

  def __str__(self):
      return str(self.table)
