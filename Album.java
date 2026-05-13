package paq;

import java.util.ArrayList;

public class Album {
    private ArrayList<Lamina> laminas = new ArrayList<>();
    private int totalLaminas = 100; 

    public void registrarLamina(Lamina nueva) {
        for (Lamina l : laminas) {
            if (l.getNumero() == nueva.getNumero()) {
                l.aumentarCantidad();
                return;
            }
        }
        nueva.aumentarCantidad();
        laminas.add(nueva);
    }

    public void mostrarColeccion() {
        for (Lamina l : laminas) {
            System.out.println(l.mostrarInfo() +
                    " | Cantidad: " + l.getCantidad());
        }
    }

    public void mostrarRepetidas() {
        for (Lamina l : laminas) {
            if (l.esRepetida()) {
                System.out.println(l.mostrarInfo());
            }
        }
    }

    public int cantidadRepetidas() {
        int c = 0;
        for (Lamina l : laminas) {
            if (l.esRepetida()) c++;
        }
        return c;
    }

    public double porcentajeLlenado() {
        return (laminas.size() * 100.0) / totalLaminas;
    }

    public void mostrarFaltantes() {
        System.out.println("Faltan " + (totalLaminas - laminas.size()) + " láminas");
    }
}