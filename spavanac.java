import java.util.Scanner;
public class spavanac {
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int H = Integer.parseInt(sc.next());
            int M = Integer.parseInt(sc.next());
            if (M >= 45) {
                M -= 45;
            }else{
                M = 60 + (M - 45);
                if (H == 0) {
                    H = 23;
                }else{
                    H--;
                }
            }
            System.out.println(H+" "+M);
        }
    }
    
}