public class Main {
    public static void main(String[] args) {

        printStar(6);

    }

    static void printStar(int n) {
        if (n>1) {
            printStar(n-1);
        }
        for (int i=0; i<n; i++) {
            System.out.println("*");

        }
    }
}
