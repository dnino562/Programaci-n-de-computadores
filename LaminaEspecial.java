package paq;

public class LaminaEspecial extends Lamina {

    private String tipo;

    public LaminaEspecial(int numero,
                          Equipos equipo,
                          String tipo) {

        super(numero, equipo);

        this.tipo = tipo;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String mostrarInfo() {
    	
        return "Especial: " + tipo +
               " | Equipo: " + equipo.getNombre();
    }
}