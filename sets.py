#sets are {}, unordered and immutable but adds ok, no dublicates
languages = {"C", "PHP", "React", "C++", "Java", "Javascript", "SQL", "Python","HTML", "CSS"}

#for x in languages:
#    print(x)

#languages.add ("MongoDB")
#print(languages)
#print(languages.clear ())
#print(languages.copy())
#languages.remove("Java")
#print(languages)
#languages.pop()
#print(languages)
languages.discard("PHP")
print(languages)
