prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if(letter not in 'OQ'):
      print(letter + suffix)   
    else:
      print(letter + 'k' + suffix)