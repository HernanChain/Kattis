import java.util.ArrayList;
import java.util.Scanner;
public class pot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String Pi = sc.next();
            StringBuilder Pi_str = new StringBuilder(Pi);
            int last = Pi_str.toString().length()-1;
            int pow = Integer.parseInt(String.valueOf(Pi.charAt(last)));
            Pi_str.deleteCharAt(last);
            int op = (int) Math.pow(Integer.parseInt(Pi_str.toString()),pow);
            list.add(op);
        }
        int sum = 0;
        for (Integer list1 : list) {
            sum += list1;
        }
        System.out.println(sum);
    }
}