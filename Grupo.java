package paq;

import java.io.Serializable;

public class Grupo implements Serializable {
    private static final long serialVersionUID = 1L;

    private String nombre;

    public Grupo(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }
}