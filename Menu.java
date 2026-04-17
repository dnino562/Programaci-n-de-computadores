package pck;
import java.util.Scanner;

public class Menu {

    public static int mostrarMenu() {
        Scanner lea = new Scanner(System.in);
        System.out.println("===== MENÚ =====");
        System.out.println("1. Ingresar datos");
        System.out.println("2. Mostrar datos");
        System.out.println("3. Salir");
        System.out.println("Seleccione una opción:");
        return lea.nextInt();
    }

    public static void main(String[] args) {
    	Scanner scanner = new Scanner(System.in);

        int opcion = 0;
        String nombre = "";
        int edad = 0;
        boolean control = true;

        while (control) {
            opcion = mostrarMenu();

            if (opcion == 1) {
                System.out.println("Ingrese su nombre:");
                scanner.nextLine(); 
                nombre = scanner.nextLine();

                System.out.println("Ingrese su edad:");
                edad = scanner.nextInt();

            } else if (opcion == 2) {
                System.out.println("Su nombre es " + nombre);
                System.out.println("Su edad es " + edad);

            } else if (opcion == 3) {
                System.out.println("Saliendo del programa");
                control = false;

            } 
            else {
                System.out.println("Número no válido");
            }
        }
    }
}