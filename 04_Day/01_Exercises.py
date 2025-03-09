#1
cadena1=''.join(["Thirty",'',"Days",'',"Of",'',"Python"])
print (cadena1)
#2
cadena2=''.join(["Coding",'',"For",'',"All"])
print (cadena2)
#3
company= "Coding For All"
#4
print(company)
#5
print(len(company))
#6
company_M= company.upper()
print(company_M)
#7
company_m= company.lower()
print(company_m)
#8
company= company.capitalize()
print(company)

company= company.title()
print(company)

company= company.swapcase()
print(company)
#9
cortarpalabra= company.split()[0]
print(cortarpalabra)
#10
if'coding' in company:
 print('la cadena tiene la palabra coding')
#11 
Remplazar=company.replace('coding','Python')
print(Remplazar)
#12
company2='Python For Everyone'
company21=company2.replace('Everyone','All')
print(company21)
#13
company.split()
print(company.split())
#14
C3="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(C3.split(','))
#15
print(company[0])
#16
print(len(company)-1)
#17
print(company[10])
#18
acronym =''.join([word[0].lower() for word in company2.split()]).upper()
print(acronym)
#19
acronym2=''.join([word[0].lower()for word in company.split()]).upper()
print(acronym2)
#20
print(cadena2.index('C'))
#21
print(cadena2.index('F'))
company121="Coding For All People"
#22
print(company121.rfind('l'))
#23
Oraciòn="You cannot end a sentence with because because because is a conjunction"
print(Oraciòn.find('because'))
#24
print(Oraciòn.rindex('because'))
#25
cortar_oración=Oraciòn.replace ('because because because','')
print(cortar_oración)
#26
posi_primerOcu= Oraciòn.index('because')
print(posi_primerOcu)
#27 aqui se repite la misma instruccion del ejercicio 25
#28
print(company.startswith('Coding'))
#29
print(company.endswith('Coding'))
#30
company122='Coding For All'
print(company122.strip())

#31
Var_1= "30DaysOfPython"
Var_2= "thirty_days_of_python"
print(Var_1.isidentifier())
print(Var_2.isidentifier())

# 32
Biblio= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(Biblio))

#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\tAge\tCountry\tCity")
print("Ely\t18\tMexico\tJalisco")

# 35
Radi= 10
Áre= 3.14 * Radi ** 2
print(f"The area of a circle with radius {Radi} is {Áre} meters square.")

# 36
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 * 6 = {8 * 6}")