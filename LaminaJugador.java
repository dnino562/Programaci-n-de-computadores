package paq;

public class LaminaJugador extends Lamina {
    private String jugador;

    public LaminaJugador(int numero, Equipo equipo, String jugador) {
        super(numero, equipo);
        this.jugador = jugador;
    }

    @Override
    public String mostrarInfo() {
        return "Jugador: " + jugador +
               " | Equipo: " + equipo.getNombre() +
               " | Número: " + numero;
    }
}