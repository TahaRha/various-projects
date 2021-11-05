public class TestStatic {

    static int x;
    int y;

    TestStatic() {
        x += 2;
        y += 3;
    }

    public static void main(String[] args) {
        TestStatic t= new TestStatic();
        t = new TestStatic();
        System.out.print(t.x);
        System.out.print(t.y);
    }
}
