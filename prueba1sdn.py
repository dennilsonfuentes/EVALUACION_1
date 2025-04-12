#Punto B-a PRUEBA1

#print("Evaluación N°1 Programación y Redes Virtualizadas")
#print("Integrantes:")
#print("- Lorenzo López")
#print("- Dennilson Fuentes")
#print("- Diego Gomez")
#print("- Alejandro López")

#Punto B-b PRUEBA1

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#codigo_sección = input("Ingrese su sección: ")
#sede = input("Ingrese su sede: ")


#print("\nInformación ingresada:")
#print("\n****************************")
#print(f"Nombre: {nombre}")
#print(f"Apellido: {apellido}")
#print(f"Código sección: {codigo_sección}")
#print(f"Sede: {sede}")
#print("\n****************************")

#Punto B-c PRUEBA1

numero_acl = int(input("Ingrese el número de ACL Ipv4: "))
if 1 <= numero_acl <= 99 or 1300 <= numero_acl <= 1999:
    print("Es una ACL Standard.")
elif 100 <= numero_acl <= 199 or 2000 <= numero_acl <= 2699:
    print("Es una ACL Extendida.")
else:
    print("El número no corresponde a una lista de acceso válida.")

