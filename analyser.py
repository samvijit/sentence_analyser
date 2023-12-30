from string import ascii_uppercase, ascii_lowercase, punctuation, digits

def analyser(str_:str)->dict:
     l_ = list(str_)
     low:int = 0
     upp:int = 0
     dig:int = 0
     pun:int = 0
     for i in l_:
          s_ = i
          if s_ in ascii_lowercase:
               low+=1
          elif s_ in ascii_uppercase:
               upp+=1
          elif s_ in digits:
               dig+=1
          elif s_ in punctuation:
               pun+=1
     return {
          "low":low,
          "upp":upp,
          "dig":dig,
          "pun":pun
     }

a = analyser("This is a Test text in which you may find 12 @3 4-0095934%680&)$(@*)(83-9=-302=318428349")
print(a)