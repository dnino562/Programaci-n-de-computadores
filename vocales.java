package pck;

import java.util.Scanner;

public class vocales {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese una cadena: ");
        String cadena = scanner.nextLine();

        cadena = cadena.toLowerCase();
        int contador = 0;

        for (int i = 0; i < cadena.length(); i++) {
            char a = cadena.charAt(i);

            if ((a == 'a') || (a == 'e') || (a == 'i') || (a == 'o') || (a == 'u')) {
                contador++;
            }
        }

        System.out.println("Número de vocales: " + contador);
        scanner.close();
    }
}