from Family.utils import parseFamilies

families = parseFamilies('Mr. Mario Mucalo, Mrs. Paola Gemić, Mrs. Ana Mucalo, Tonka Mucalo, Mr. Juraj Gemić, Lara Gemić, Toma Mucalo')

print(families[0].toString())
print(families[1].toString())