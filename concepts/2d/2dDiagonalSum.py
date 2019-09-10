#Given a two day array with same number of rows and columns
#Write a function that adds up all diagnol elments and returns the sum\
def diagonal_sum(given_2d):
  total = 0
  for i in range(len(given_2d)):
    total += given_2d[i][i]
  return total
