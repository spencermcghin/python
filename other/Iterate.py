__author__ = 'SMcGhin'
for x in range(1, 101):
   a = ""
   if x % 4 == 0:
       a += "Go"
   if x % 5 == 0:
       a += "Figure"
   if a == "":
       a = x
   print a