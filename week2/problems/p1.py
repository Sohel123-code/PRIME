# given dictionary of tupples we need to access unique subjects
info ={
    ("alice","english"),
    ("shyam","english"),
    ("bob","maths"),
  ("charlie","physics"),
 ("david","english"),
  ("emma","chemistry"),
 ("frank","biology"),
 ("george","maths"),
 ("harry","computer"),
 ("irfan","english"),
  ("jithendra","physics"),
}


s=set()
for tup in info :
    s.add(tup[1])
    

print(s)

# students enrolled in english

print("Students enrolled for english are")
for f,n in info:
    if(n=="english"):

        print(f)
