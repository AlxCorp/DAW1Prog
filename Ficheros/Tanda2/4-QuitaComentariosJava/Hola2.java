/*
Este programa calcula la suma de dos números enteros.

Para utilizarlo, simplemente ingresa los números que deseas sumar como argumentos en la línea de comandos al ejecutar el programa.
*/

public class SumaNumeros {
    public static void main(String[] args) {
        
        if (args.length != 2) {
            System.err.println("Debes proporcionar dos números como argumentos.");
            System.exit(1);
        }

        
        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);
        int suma = num1 + num2;

        
        System.out.println("La suma de " + num1 + " y " + num2 + " es " + suma + ".");
    }
}
