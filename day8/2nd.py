alphabet=['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encode(text,shift):
    cipher_text=""
    for i in text:
        if i in alphabet:
            x=alphabet.index(i)
            new=x+shift
            if(new>=len(alphabet)):
                new=new-len(alphabet)
            cipher_text+=alphabet[new]
        else:
            cipher_text+=i
    return cipher_text

def decode(cipher_text,shift):
    text=""
    for i in cipher_text:
        if i in alphabet:
            x=alphabet.index(i)
            new=x-shift
            if(new<0):
                new=new+len(alphabet)
            text+=alphabet[new]
        else:
            text+=i
    return text

print("welcome to umesh encoder!!😎\n")
print('''
+-++-++-++-++-+
|u||m||e||s||h|
+-++-++-++-++-+
+-++-++-++-++-++-++-+
|e||n||c||o||d||e||r|
+-++-++-++-++-++-++-+
''')

want=True
while want:
    direction=input("type 'encode' to encrypt and 'decode to decrypt': \n")
    text=input("type the message: ").lower()
    shift=int(input("type shift number:\n"))
    if direction=="encode":
        if shift>len(alphabet):
            shift=shift%len(alphabet)
        text=encode(text,shift)
        print(f"encoded text is {text}")
    elif direction=="decode":
        if shift>len(alphabet):
            shift=shift%len(alphabet)
        text=decode(text,shift)
        print(f"decoded message is : {text}")
    else:
        print("wrong input!")
    user=input("\nyou want to go again (y/n): ")
    if user=='y':
        want=True
    else:
        want=False
