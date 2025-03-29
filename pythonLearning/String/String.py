

# Revert String 5 ways program:
str = "i.like.this.program.very.much"
s = str.split(".")

for x in s:
    reverse_sentence = '.'.join(reversed(s))
    print(reverse_sentence)

s1 = "pqr.mno"
s2 = s1.split(" ")
for i in s1:
    rev = ''.join(reversed(s2))
    print(rev)

txt = "Hello World"
def reverse(text):
    result = ""
    for i in range(len(text),0,-1):
        result += text[i-1]
    return (result)

reverse(txt)