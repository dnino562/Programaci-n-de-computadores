package paq;
import java.util.Scanner;

public class Notas {
    
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        double [] notas = new double[5];

        for (int i = 0; i < notas.length; i++) {
            notas[i] = 99;
            while (notas[i] < 0 || notas[i] > 5) {
                System.out.println("Ingrese la nota " + (i+1) + " entre 0 y 5:");
                notas[i] = sc.nextDouble();
            }
        }

        double mayor = 0;
        double menor = 5;
        double promedio = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] > mayor) {
                mayor = notas[i];
            }
            if (notas[i] < menor) {
                menor = notas[i];
            }
            promedio += notas[i];
        }

        promedio = promedio / notas.length;

        System.out.println("Nota mayor: " + mayor);
        System.out.println("Nota menor: " + menor);
        System.out.println("Nota promedio: " + promedio);
    }
}