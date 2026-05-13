package paq;

public abstract class Lamina {
    protected int numero;
    protected Equipo equipo;
    protected int cantidad;

    public Lamina(int numero, Equipo equipo) {
        this.numero = numero;
        this.equipo = equipo;
        this.cantidad = 0;
    }

    public void aumentarCantidad() {
        cantidad++;
    }

    public boolean esRepetida() {
        return cantidad > 1;
    }

    public int getCantidad() {
        return cantidad;
    }

    public int getNumero() {
        return numero;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public abstract String mostrarInfo();
}