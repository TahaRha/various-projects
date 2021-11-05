import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    String x = "2";
    System.out.println(x.clone() == x);
    System.out.println(x.clone().equals(x));
    

  }
}

