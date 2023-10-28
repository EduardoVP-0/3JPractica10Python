#PRACTICA10
#EDUARDOVELAZQUEZ
def sumaIterativa(n):
	suma = 0

	while n > 9:
		suma += n % 10;
		n //= 10;

	return suma + n

def sumaRecursiva(n):
	if n <= 9:
		return n
	else:
		return sumaRecursiva(n//10) + n%10

n = int(input("Ingrese n: "))
print("El resultado de la suma iterativa es: ",sumaIterativa(n))
print("El resultado de la suma recursiva es: ",sumaRecursiva(n))
