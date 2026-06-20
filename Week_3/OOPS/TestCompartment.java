import java.util.Random;

abstract class Compartment {
    public abstract String notice();
}
class FirstClass extends Compartment {

    public String notice() {
        return "Welcome to First Class";
    }
}
class Ladies extends Compartment {

    public String notice() {
        return "Ladies Compartment";
    }
}
class General extends Compartment {

    public String notice() {
        return "General Compartment";
    }
}
class Luggage extends Compartment {

    public String notice() {
        return "Luggage Compartment";
    }
}
public class TestCompartment {

    public static void main(String[] args) {

        Compartment[] arr = new Compartment[10];

        Random r = new Random();

        for (int i = 0; i < 10; i++) {

            int n = r.nextInt(4) + 1;

            if (n == 1)
                arr[i] = new FirstClass();
            else if (n == 2)
                arr[i] = new Ladies();
            else if (n == 3)
                arr[i] = new General();
            else
                arr[i] = new Luggage();

            System.out.println(arr[i].notice());
        }
    }
}
