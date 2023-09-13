s = "abcdefghijklmnopqrstuvwxyz"
print(s)

print(s[0], s[4])

print(s[-1])

print(s[4:10])

def toLowerCase(v: str):
  return v.lower()

print(toLowerCase("SHOULD BE IN LOWER CASE"))

def repl(v: str):
  return v.replace("tu", "ta")

print(repl("tutu on the tuji-kata"))

string = "hello world"
position = string.find("a")
print(position)

p = "abcdefghij"
print(p[::-2][:5][::-1][3:])

def repeat(v):
  for i in range(0, 10):
    print(f'{i}: {v}')
    
repeat("salut")

s1 = "Hello"
s2 = 42
concat = s1 + str(s2)
print(concat)

string1 = "42"
string2 = "is"
string3 = "the answer"
concat = f"{string1} {string2} {string3}"
print(f"The string {concat} characters")

def occurences(v: str):
  words = ["cat", "garden", "mice"]
  lowered = v.lower()
  reversed = lowered[::-1]
  count = 0
  for word in words:
    count += lowered.count(word) + reversed.count(word)
  return count

print(occurences("“thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))

#ipt = input("Enter your username: ")
#print(f"Hello {ipt.capitalize()}")

#ipt1 = int(input("Enter first number: "))
#ipt2 = int(input("Enter second number: "))
#print(f"{ipt1 + ipt2} - {ipt1.__class__}")

a = "This is a test. Is it possible to fly? Good things come to those who never give up."
tmp = None
separator = [".", "?"]
for s in separator:
  if tmp is None:
    tmp = a.split(s)
  else:
    for i in range(0, tmp.__len__()):
       v = tmp[i]
       tmp.pop(i)
       t = str(v).split(s)
       for j in range(0, t.__len__()):
         tmp.insert(i+j, t[j])
    
new = []
for t in tmp:
  new.append(t.strip().split(" ")[0])
  
print(" ".join(new))

