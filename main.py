import secrets

def block_message(message):

  block_1 = message[0:9]
  block_2 = message[9:19]
  block_3 = message[19:29]
  block_4 = message[29:40]
  block_5 = message[40:49]
  block_6 = message[49:50]
  block_7 = message[50:59]
  block_8 = message[59:60]

  #print("message length: ", len(message))
  #print("block 1: ", block_1, "block_2: ", block_2, "block 3: ", block_3)
  return block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8

def generate_key_256bit():

  global key
  
  key = secrets.randbits(256)  # Generate a 128-bit key
  print("\n256-bit key:", key)
  return key

def convert_to_ascii(message):

  global ascii_values
  
  ascii_values = [ord(char) for char in message]
  #print("ascii values", ascii_values)
  
  return ascii_values

def encrypt(ascii_values, key):

  global encrypted_message
  
  encrypted_message = [value * key for value in ascii_values]
  print("\nencrypted message: ", encrypted_message)
  #print("encrypted message length: ", len(encrypted_message))
  return encrypted_message

def decrypt(ascii_values, key):

  unlocked_message = [value // key for value in encrypted_message]
  
  #print("decrypted values: ", unlocked_message)

  decrypted_message = (''.join(chr(value) for value in unlocked_message))

  print("\noriginal message: ", decrypted_message)
  return decrypted_message

message = input("Enter a message: ")

block_message(message)
generate_key_256bit()
convert_to_ascii(message)

encrypt(ascii_values, key)
decrypt(ascii_values, key)