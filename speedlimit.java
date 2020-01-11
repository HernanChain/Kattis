import java.util.Scanner;
public class speedlimit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            String iterable = sc.next();
            if (Integer.parseInt(iterable) != -1) {
                int[] speeds;
                speeds = new int[Integer.parseInt(iterable)];
                int[] times = new int[speeds.length];
                for (int i = 0; i < Integer.parseInt(iterable); i++) {
                    speeds[i] = Integer.parseInt(sc.next());
                    times[i] = Integer.parseInt(sc.next());
                }
                int sum = 0;
                for (int i = 0; i < speeds.length; i++) {
                    if (i == 0) {
                        sum += speeds[i] * times[i];
                    } else {
                        sum += speeds[i] * (times[i] - times[i - 1]);
                    }
                }
                System.out.println(sum+ " miles");
            }
        }
    }
}