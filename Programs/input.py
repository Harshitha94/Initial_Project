print ("To play, keep on pressing any of these keys: c d e f g a b")
print ("Press q to stop")
i=1
if i==1:
    note= ord(input())
    i=0
print (note)
while True:
    print(note)
    i=1
    print (note),
    if i==1:
        note = ord(input())
        i=0
    if note==ord('q'):
        break
    
    
