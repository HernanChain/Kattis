import java.util.Scanner;
public class easiest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String linea = sc.next();
            if (Integer.parseInt(linea) != 0) {
                int multiplicador = 11;
                while (true) {
                    int res = Integer.parseInt(linea) * multiplicador;
                    if (new easiest().sumDigits(linea) == new easiest().sumDigits(String.valueOf(res))) {
                        System.out.println(multiplicador);
                        break;
                    } else {
                        multiplicador++;
                    }
                }
            } else {
                break;
            }
        }
    }

    public int sumDigits(String line) {
        int sumLinea = 0;
        for (int i = 0; i < line.length(); i++) {
            sumLinea += Integer.parseInt(String.valueOf(line.charAt(i)));
        }
        return sumLinea;
    }

}