package paq;

public class Lamina {

    protected final int numero;
    protected final Equipos equipo;
    protected int cantidad;

    public Lamina(int numero, Equipos equipo) {
        this.numero = numero;
        this.equipo = equipo;
        this.cantidad = 0;
    }

    public void aumentarCantidad() {
        cantidad++;
    }

    public int getCantidad() {
        return cantidad;
    }

    public boolean esRepetida() {
        return cantidad > 1;
    }

    public int getNumero() {
        return numero;
    }

    public Equipos getEquipo() {
        return equipo;
    }

}