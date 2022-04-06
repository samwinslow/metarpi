def chunk(string, n):
  """Chunk into an array of strings of n characters each"""
  return [string[i:i+n] for i in range(0, len(string), n)]
