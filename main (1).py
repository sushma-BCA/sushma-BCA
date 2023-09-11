


def isleapyear(year):
  if(year/4==0 and year/100!=0) or year/ 400==0:
    return True
  else:
    return False
year=2020
if isleapyear(year):
  print("2020 is a leap year ")
else:
  print("2020 is a not a leap year")
      