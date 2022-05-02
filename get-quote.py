import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #last = len(quotes-1) if you want to add or remove quotes from your text file, change the last variable to update automatically
  last = 13
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
