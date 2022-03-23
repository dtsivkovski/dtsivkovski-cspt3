class Palindrome:
  def __init__(self):
        self.filtered = ""
        self.paliBool = True

  def __call__(self, n):
    self.filtered = ""
    self.paliBool = True
    # Filters the string for letters only and appends them to the filtered string
    for i in n:
      if i.isalpha():
        self.filtered += i
    # For loop for palindrome finding
    
    print("="*45, "\nString: ", n,"\n" , '-'*44)
    for i in range(0, int(len(self.filtered)/2)):
      
      # Sets a to the lowercase of the letter that is i position in the string
      a = self.filtered[i].lower()
      # Sets b to the lowercase of the letter that is i amount starting from the end of the string
      b = self.filtered[(len(self.filtered) - i - 1)].lower()
      if a != b:
        # Breakpoint if the letters do not match to state it is not a palindrome
        self.paliBool = False
        print("'" + n + "'", "is not a palindrome at position " + str(i) +  " because", a, "!=", b)
        break
    # Print statement if the word is a palindrome (boolean stayed true)
    if self.paliBool:
      print("'" + n + "'", "is a palindrome!")
    

def pali_tester():
  pali = Palindrome()
  print("")
  # racecar tester, should output true
  pali("racecar")
  # test for case and symbol sensitivity, should output true
  pali("rACe_cA--R")
  # not a palindrome, should be false
  pali("racing car")
  # another test for space/symbol/case sensitivity, should be true
  pali("A man, a plan, a canal -- Panama!")
  print("")