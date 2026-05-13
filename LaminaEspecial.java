package paq;

public class LaminaEspecial extends Lamina {
    private String tipo;

    public LaminaEspecial(int numero, Equipo equipo, String tipo) {
        super(numero, equipo);
        this.tipo = tipo;
    }

    @Override
    public String mostrarInfo() {
        return "Especial: " + tipo +
               " | Equipo: " + equipo.getNombre() +
               " | Número: " + numero;
    }
}