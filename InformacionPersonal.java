package pck;

import java.util.Scanner;

public class InformacionPersonal {
	
	public static void main (String[] args) {
		//TODO Auto-generated method stub
		
		Scanner sc= new Scanner(System.in);
		System.out.println("Nombre: Danna Alejandra Niño Abril\n"
				+ "Edad:18\n"
				+ "Programa:Ing.Biomedica");
		
		//print("Nombre: Danna Alejandra Niño Abril\nEdad:18\nPrograma:Ing.Sistemas")
		
		String nombre= "Danna Alejandra Niño Abril";
		int edad=18 ;
		String programa="Ing.Biomedica";
		System.out.println(nombre+"\n"+edad+"\n"+ programa);
		System.out.println("Cual es tu nombre:");
		nombre=sc.nextLine();
		System.out.println("Cual es tu edad:");
		edad=sc.nextInt();
		sc.nextLine();
		System.out.println("Cual es tu carrera:");
		programa=sc.nextLine();
		System.out.println(nombre+"\n"+edad+"\n"+ programa);
		
		//----------------------------------------------------//
		int opcion = menu();
		System.out.println("opcion seleccionada"+opcion);
	}
	
	public static int menu() {
		Scanner scanner = new Scanner(System.in);
		int opcion = -1;
		
		while (opcion != 0) {
		System.out.println("-- MENÚ DE OPCIONES ---");
		System.out.println("1. Saludar");
		System.out.println("2. Hablar");
		System.out.println("3. Despedirse");
		System.out.println("4. Salir");
		System.out.println("5. Terminar");
		System.out.print("Seleccione el numero asignado a la opcion que desee seguir ");
	}
	return opcion;
	}
}
