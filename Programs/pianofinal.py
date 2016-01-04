import string
from winsound import Beep
from msvcrt import getch
def play_note(frequency, duration):
    Beep(frequency, duration)
a = 440
twelfth_root_2 = 2 ** (1.0/12.0)
tr2 = twelfth_root_2
tr2sqrd = tr2 * tr2
b = int(round(a * tr2sqrd))
g = int(round(a / tr2sqrd))
f = int(round(g / tr2sqrd))
e = int(round(f / tr2sqrd))
d = int(round(e / tr2sqrd))
c = int(round(d / tr2sqrd))
print "c =", c, "d =", d, "e =", e, "f =", f
print "g =", g, "a =", a, "b =", b
notes = {}
notes['c'] = c
notes['d'] = d
notes['e'] = e
notes['f'] = f
notes['g'] = g
notes['a'] = a
notes['b'] = b
print "To play, keep on pressing any of these keys: c d e f g a b"
print "Press q to stop"
duration = 300 
note = string.lower(getch())
while True:
    print note,
    if note in notes:
        play_note(notes[note], duration)
    elif note == 'q':
        break
    note = string.lower(getch())
