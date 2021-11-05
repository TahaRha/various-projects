public class Memory {
    private String name;

    public Memory(String name) {
        this.name = name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public static void main(String args[]) {
        Memory myDog = new Memory("Champion");
        myDog.name = "Hamid";
        System.out.println(myDog.name);
    }
}
