package paq;

public class Equipos {
	private String nombre;
	private String letras;
	private String grupo;
	
	public Equipos(String nombre, String letras, String grupo, String laminas) {
		super();
		this.nombre = nombre;
		this.letras = letras;
		this.grupo = grupo;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getletras() {
		return letras;
	}
	public void setLetras(String letras) {
		this.letras = letras;
	}
	public String getGrupo() {
		return grupo;
	}
	public void setGrupo(String grupo) {
		this.grupo = grupo;
	}
	
}
