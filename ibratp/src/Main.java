import java.util.Scanner;
import java.util.LinkedList;

public class Main {

    private static int[] quantities = new int[6];

    public static void order() {
        String[] menu = new String[6];
        menu[0] = "Frites de vers";
        menu[1] = "Brochettes mexicaines aux cucarachas";
        menu[2] = "Pizza aux sauterelles (petite)";
        menu[3] = "Pizza aux sauterelles (moyenne)";
        menu[4] = "Le burger Scarabée";
        menu[5] = "Macaron aux grillons";

        double[] prices = new double[6];
        prices[0] = 2.5;
        prices[1] = 1.25;
        prices[2] = 8;
        prices[3] = 12;
        prices[4] = 7;
        prices[5] = 1.25;

        LinkedList<String> facture = new LinkedList();

        System.out.println("***-----<>-----***\n * Chez Bibitte * \n***-----<>-----***");

        Scanner userinput = new Scanner(System.in);
        String orderInput = "";
        int count=0;
        while (! orderInput.equals("7")) {
            count++;
            System.out.println("Choisir un item dans le menu \n----------------------------");

            for (int i = 1; i < menu.length+1; i++) {
                System.out.println(i + "- "+ menu[i-1] + "\t\t\t" + prices[i-1] + "$ chacune");

            }
            if (count > 1) {
                System.out.println("7- Générer la facture");
            }

            orderInput = userinput.nextLine();
            if (Integer.parseInt(orderInput) > 7) {
                System.out.println("Invalid input");
                System.exit(1);
            }
            if (! orderInput.equals("7")) {
                System.out.println("Quelle quantité?");
                String quantityInput;
                quantityInput = userinput.nextLine();

                facture.add(new String (orderInput+quantityInput));

            }

        }
        System.out.println("Facture \n----------------------------");
        for (String element: facture) {
            int product = Character.getNumericValue(element.charAt(0))-1;
            String strQuantity= "";
            for (int i=1; i < element.length(); i++) {
                strQuantity += element.charAt(i);
            }
            int quantity = Integer.parseInt(strQuantity);
            System.out.println(menu[product] + " x " + quantity + "\t\t\t" + quantity*prices[product]);
        }
        System.out.println("----------------------------");
        double total= 0;
        for (String element: facture) {
            int product = Character.getNumericValue(element.charAt(0))-1;
            String strQuantity= "";
            for (int i=1; i < element.length(); i++) {
                strQuantity += element.charAt(i);
            }
            int quantity = Integer.parseInt(strQuantity);

            total += quantity*prices[product];
        }
        double rabais= 0;
        if (total < 100 && total > 50) {
            rabais = total*0.05;
        }
        else if (total >= 100) {
            rabais = total*0.1;
        }
        double TAXES= 0.15*(total-rabais);

        double totalFinal= total+rabais+TAXES;

        System.out.println("sous-total: \t\t\t"+ total);
        System.out.println("rabais: \t\t\t"+ rabais);
        System.out.println("TAXES: \t\t\t"+ TAXES);
        System.out.println("----------------------------");
        System.out.println("Prix final: \t\t\t"+ totalFinal);

        LinkedList<String> orderedElements= new LinkedList();
        LinkedList<Integer> quantityElements= new LinkedList();

        for (String element: facture) {
            String strQuantity= "";
            for (int i=1; i < element.length(); i++) {
                strQuantity += element.charAt(i);
            }
            int quantity = Integer.parseInt(strQuantity);


            quantities[Character.getNumericValue(element.charAt(0))-1] += quantity;
        }

    }
    public static void main(String args[]) {
        String[] menu = new String[6];
        menu[0] = "Frites de vers";
        menu[1] = "Brochettes mexicaines aux cucarachas";
        menu[2] = "Pizza aux sauterelles (petite)";
        menu[3] = "Pizza aux sauterelles (moyenne)";
        menu[4] = "Le burger Scarabée";
        menu[5] = "Macaron aux grillons";

        int numberOrders = 0;
        Scanner userinput = new Scanner(System.in);
        String afterOrder= "1";



        while (afterOrder.equals("1")) {
            order();
            System.out.println("Choisir un item dans le menu \n----------------------------");
            System.out.println("1- Nouvelle commande \n2- Quitter");
            afterOrder = userinput.nextLine();
            numberOrders++;

        }

        System.out.println("Nombre de commandes aujourd'hui: "+ numberOrders);
        System.out.println("----------------------------");
        for (int i=0; i< menu.length; i++) {
            if (quantities[i] != 0) {
                System.out.println(menu[i] + " x " + quantities[i]);
            }
        }
        System.out.println("----------------------------\nAu revoir !!!!");

    }
}


