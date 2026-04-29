package pck;

import java.util.Scanner;

public class VariasNotas {
	public static void main(String[] args) {
		Scanner lea = new Scanner(System.in);
		String[] estudiantes = new String[5];
		int[] edades = new int[5];
		double [][] notas = new double [5][3];
		System.out.println(notas[0].length);
		for(int i = 0; i < edades.length; i++) {
			System.out.println("Ingrese el nombre " + (i+1));
			estudiantes[i] = lea.nextLine();
			System.out.println("Ingrese la edad ");
			edades[i] = lea.nextInt();
			lea.nextLine();
			for (int j = 0; j < 3; j++) {
				notas [i][j]=99;
				while (notas [i][j]<0 || notas [i][j]> 5) {
					System.out.println ("Ingrese la nota " + (i+1) + "entre 0 y 5");
					notas [i][j] = lea.nextDouble();
				}
			}
			lea.nextLine();
		}
        
        for (int k = 0; k < edades.length; k++) {
        	System.out.println(estudiantes[k]+ " edad: " + edades[k]);
            double mayor = 0;
            double menor = 5;
            double promedio = 0;
        	for (int m = 0; m < notas[k].length; m++) {
        		if (mayor < notas [k][m]) {
        			menor = notas [k][m];
            }
            if (menor > notas [k][m]) {
                menor = notas[k][m];
            }
            promedio += notas[k][m];
        }

        promedio = promedio/notas[k].length;

        System.out.println("Nota mayor: " + mayor);
        System.out.println("Nota menor: " + menor);
        System.out.println("Nota promedio: " + promedio);
	 }
	}
}
