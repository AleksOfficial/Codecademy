# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressing", "distressed", "concerning", "horrible", "horribly", "questionable"]

def encryptor_one_word(word,email):
  length = len(word)
  new_mail =""
  i = 0
  
  while i < len(email):
    to_be_encrypted = email[i:i+length]
    if(to_be_encrypted==word.lower() or to_be_encrypted==word.upper() or to_be_encrypted==word.title() or to_be_encrypted==word):
      for j in range(length):
        new_mail+="#"
        i+=1
    else:
      new_mail += email[i]
      i+=1
  return new_mail

def encryptor_several_words(words,email):

  new_mail =""
  i = 0
  
  while i < len(email):
    for j in words:
      length = len(j)
      to_be_encrypted = email[i:i+length]
      if(to_be_encrypted==j.title() or to_be_encrypted==j.upper() or to_be_encrypted==j.lower() or to_be_encrypted==j):
        for y in range(length):
          new_mail+="#"
          i+=1
      else:
        continue
    new_mail += email[i]
    i+=1

  return new_mail

def encryptor_bad_language(neg_words,prop_words,email):
  
  all_words = neg_words + prop_words
  i = 0
  count = 0
  new_mail = ""

  while i < len(email):
    for trigger in neg_words:
      lengthtrig = len(trigger)
      lol = email[i:i+lengthtrig]
      if(trigger == lol and count <=2 or trigger.upper() == lol and count <=2 or trigger.title() == lol and count <=2 or trigger.lower() == lol and count <=2 ):
        count +=1
        continue

      elif(count >2):
        for j in all_words:
          length = len(j)
          to_be_encrypted = email[i:i+length]
          if(to_be_encrypted==j.title() or to_be_encrypted==j.upper() or to_be_encrypted==j.lower() or to_be_encrypted==j):
            for y in range(length):
              new_mail+="#"
              i+=1
          else:
            continue

    new_mail += email[i]
    i+=1

  return new_mail

def encryptor_all(negative_words,proprietary_terms,email):
  pre_mail =""
  new_mail=""
  pre_mail=encryptor_bad_language(negative_words,proprietary_terms,email)
  for i in pre_mail:
    x = ord(i)
    if(x>= 97 and x<= 122):
      new_mail+='#'
    elif(x>=65 and x<= 90):
      new_mail+="#"
    else:
     new_mail += i
  return new_mail
#Emailone      
#print(email_one)
#print("\n\nEncrypted:\n")
#print(encryptor_one_word("learning algorithms",email_one))

#Emailtwo 
# print("\n")
# print(email_two)
# print("\n\nEncrypted:\n")
# print(encryptor_several_words(proprietary_terms,email_two))
lola = None
#Emailthree   
# print("\n")
# print(email_three)
# print("\n\nEncrypted:\n")
# print(encryptor_bad_language(negative_words,proprietary_terms,email_three))

#Emailfour
print(email_four)
print("\n\nEncrypted:\n")
print(encryptor_all(negative_words,proprietary_terms,email_four))
print(lola)
#eof  