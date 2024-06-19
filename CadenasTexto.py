s1 = "Myroslava"
s2 = "Sofia"
s3 = "Galina"

# Concatenation
print(s1 + "," + s2 + " " + s3 + "!")
print(s1*3)

# Indexing
print(s1[0], s1[1], s1[2], s1[3], s1[4], s1[5], s1[6], s1[7], s1[8])
print(s2[1], s2[2:5])
print(s3[0:4])

# Length
print(len(s1))

# Slicing
print(s1[0:4])
print(s2[0:3])

# find
print("m" in s1.lower())

# replace
print(s1.replace("Myroslava", "Olesya"))

# split
print(s1.split("r"))

# upper
print(s1.upper())
print(s2.lower())
print(s3. capitalize())
print(s1.title())

# Eliminación de espacios al principio y al final
print("Myroslava".strip())

# busqueda al principio y al final
print(s1.startswith("M"))
print(s1.endswith("a"))

#busqueda en posicion
print("Myroslava".find("r"))

# número de ocurriencias
print("Myroslava".lower().count("a"))

# Formateo

print("My name: {0}, lenguaje: {1}!".format(s1, "Python"))

#interpolacion de cadenas
print (f"Mi nombre es {s1}, mi lenguaje favorito es {s2}!")


##transformaciones de listas en cadena.
l1= [s1, s2, s3]
print(" ".join(l1))













