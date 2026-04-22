package apc;

import java.util.Scanner;

public class Menu {
	static Scanner sc = new Scanner(System.in);

    public static int mostrarMenu() {
        System.out.println("\n===== MENÚ PRINCIPAL =====");
        System.out.println("1. Mostrar números (for)");
        System.out.println("2. Sumar números (while)");
        System.out.println("3. Validar contraseña (do-while)");
        System.out.println("4. Salir");
        System.out.print("Elige una opción: ");
        return sc.nextInt();
    }
 
    //  Opción 1 – Mostrar números con FOR

    public static void mostrarNumeros(int n) {
        System.out.println("\nNúmeros del 1 al " + n + ":");
        for (int i = 1; i <= n; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
 
    //  Opción 2 – Sumar números con WHILE
    
    public static int sumarNumeros() {
        int suma = 0;
        System.out.println("Ingresa números para sumar :");
        System.out.print("Número: ");
        int numero = sc.nextInt();
        while (numero != 0) {
            suma += numero;
            System.out.print("Siguiente número: ");
            numero = sc.nextInt();
        }
        return suma;
    }
 
    //  Opción 3 – Validar contraseña con DO-WHILE
    
    public static void validarPassword() {
        final String PASSWORD_CORRECTA = "123";
        String intento;
        System.out.println("Acceso restringido");
        do {
            System.out.print("Ingresa la contraseña: ");
            intento = sc.next();
            if (!intento.equals(PASSWORD_CORRECTA)) {
                System.out.println("Contraseña incorrecta. Intenta de nuevo.");
            }
        } while (!intento.equals(PASSWORD_CORRECTA));
        System.out.println("Acceso concedido! Bienvenido.");
    }
    
    public static void main(String[] args) {
        int opcion;
 
        do {
            opcion = mostrarMenu();
 
            switch (opcion) {
                case 1:
                    System.out.print("¿Hasta qué número quieres mostrar? ");
                    int n = sc.nextInt();
                    mostrarNumeros(n);
                    break;
 
                case 2:
                    int total = sumarNumeros();
                    System.out.println("Suma total: " + total);
                    break;
 
                case 3:
                    validarPassword();
                    break;
 
                case 4:
                    System.out.println("Programa finalizado.");
                    break;
 
                default:
                    System.out.println("Opción no válida. Intenta de nuevo.");
            }
 
        } while (opcion != 4);
 
    }
}
 