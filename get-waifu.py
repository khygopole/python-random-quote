import random
def gacha():
  #print("Keep it logically awesome.")

  f = open("hololive.txt")
  waifus = f.readlines()
  f.close()
  #last = len(quotes-1) if you want to add or remove quotes from your text file, change the last variable to update automatically
  last = 72
  rnd = random.randint(0,last)
  print("Congratulations, you've got: " + waifus[rnd] + "HAPPY GACHA LIFE")
  
if __name__== "__main__":
  gacha()