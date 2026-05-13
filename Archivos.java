package paq;

import java.io.*;

public class Archivos {

    public static void guardarAlbum(Album album) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(
                new FileOutputStream("album.dat"));
        oos.writeObject(album);
        oos.close();
    }

    public static Album leerAlbum() throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(
                new FileInputStream("album.dat"));
        Album Lamina = (Album) ois.readObject();
        ois.close();
        return Lamina;
    }
}