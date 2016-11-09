Sleep In #

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# Monkey Trouble #


def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    if not a_smile and not b_smile:
        return True
    return False

# Sum Double #

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

# Diff_21 #

if n > 21:
    return abs(n - 21) * 2
  else:
    return abs(n - 21)

# Parrot Talks #

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

# Makes 10 #

def makes10(a, b):
  return (a + b == 10 or a == 10 or b == 10)

# Near 100 #

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# not_string #

def not_string(str):
  if str.startswith('not'):
    return str
  else:
    return 'not ' + str

# Missing_Char #

def missing_char(str, n):
    return str.replace(str[n], '')

# Front 3 #

def front3(str):
  str1 = str[:3]
  return str1 + str1 + str1



