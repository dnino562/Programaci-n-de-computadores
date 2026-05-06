package paq;

public class Lamina {
	private int numero;
	private String equipo;
	private String jugador;
	private boolean esEspecial;
	private int cantidad; 
	
	public Lamina(int numero, String nombre, String equipo, String jugador, boolean esEspecial) {
		super();
		this.numero = numero;
		this.equipo = equipo;
		this.jugador = jugador;
		this.esEspecial = esEspecial;
		this.cantidad = 0;
	}
	public int getNumero() {
		return numero;
	}
	public void setNumero(int numero) {
		this.numero = numero;
	}
	public String getEquipo() {
		return equipo;
	}
	public void setEquipo(String equipo) {
		this.equipo = equipo;
	}
	public String getJugador() {
		return jugador;
	}
	public void setJugador(String jugador) {
		this.jugador = jugador;
	}
	public boolean isEsEspecial() {
		return esEspecial;
	}
}

