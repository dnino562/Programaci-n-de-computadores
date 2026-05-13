package paq;

public class Equipo {
    private String nombre;
    private Grupo grupo;

    public Equipo(String nombre, Grupo grupo) {
        this.nombre = nombre;
        this.grupo = grupo;
    }

    public String getNombre() {
        return nombre;
    }

    public Grupo getGrupo() {
        return grupo;
    }
}