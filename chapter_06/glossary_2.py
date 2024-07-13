glossary = {
    "variable" : "Are used to store information to be referenced and manipulated in a computer program",
    "constant" : "A value that is not altered by the program during normal execution",
    "dictionary" : "Is a data structure that is used to store data using a key and value system",
    "tuple" : "An ordered set of values that store multiple data types",
    "parameters" : "Is a special kind of variable used in a subroutine to refer to one of the pieces of data provided as input to the subroutine"
}

for key, value in glossary.items():
    print(f"{key}:\n\t{value}")

glossary["python"] = "Is used for server-side web development, software development, mathematics, and system scripting"

for key, value in glossary.items():
    print(f"{key}:\n\t{value}")