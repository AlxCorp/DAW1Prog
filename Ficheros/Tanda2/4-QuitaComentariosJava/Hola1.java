/*
Este programa calcula la suma de dos números enteros.

Para utilizarlo, simplemente ingresa los números que deseas sumar como argumentos en la línea de comandos al ejecutar el programa.
*/

public class SumaNumeros {
    public static void main(String[] args) {
        // Verifica que se hayan proporcionado dos argumentos
        if (args.length != 2) {
            System.err.println("Debes proporcionar dos números como argumentos.");
            System.exit(1);
        }

        // Convierte los argumentos a enteros y los suma
        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);
        int suma = num1 + num2;

        // Imprime la suma de los números en la consola
        System.out.println("La suma de " + num1 + " y " + num2 + " es " + suma + ".");
    }
}
