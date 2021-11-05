import java.util.Arrays;

public class SillySwap {

    public static void main(String[] args) {
        int[] arr = new int[5];
        for (int i=0; i < arr.length ; i++) {
            arr[i] = i;
        }
        swap(arr[0], arr[4], arr);
        System.out.println(Arrays.toString(arr));
        System.out.print("zebi");
    }

    static void swap(int a, int b, int[] arr) {
        int tmp= a;
        a = b;
        b = tmp;
        tmp = arr[1];
        arr[1] = arr[3];
        arr[3] = tmp;
    }
}
