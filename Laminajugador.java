package paq;

public class LaminaJugador extends Lamina {

    private String jugador;
    private String posicion;

    public LaminaJugador(int numero,
                         Equipos equipo,
                         String jugador,
                         String posicion) {

        super(numero, equipo);

        this.jugador = jugador;
        this.posicion = posicion;
    }

    public String getJugador() {
        return jugador;
    }

    public void setJugador(String jugador) {
        this.jugador = jugador;
    }

    public String getPosicion() {
        return posicion;
    }

    public void setPosicion(String posicion) {
        this.posicion = posicion;
    }

    @Override
    public String mostrarInfo() {
        return "Jugador: " + jugador +
               " | Posición: " + posicion +
               " | Lámina #" + numero +
               " | Equipo: " + equipo.getNombre();
    }
}