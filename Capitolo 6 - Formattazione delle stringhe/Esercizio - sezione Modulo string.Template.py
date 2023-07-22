from string import Template

name = "Eva"
age = 50

template = Template("Ciao, mi chiamo $name e ho $age anni.")
message = template.substitute(name=name, age=age)
print(message)  # Output: "Ciao, mi chiamo Eva e ho 50 anni."

from string import Template

# Template con sostituzione di lista
template1 = Template("Ciao, sono $name e mi piacciono: $hobbies")
name = "Alice"
hobbies = ["pittura", "musica", "giardinaggio"]
result1 = template1.substitute(name=name, hobbies=", ".join(hobbies))
print(result1)
# output: Ciao, sono Alice e mi piacciono: pittura, musica, giardinaggio

# Template con sostituzione di dizionario
template2 = Template("Il mio nome è $name e sono di $city")
info = {"name": "Bob", "city": "New York"}
result2 = template2.substitute(info)
print(result2) #output: Il mio nome è Bob e sono di New York
