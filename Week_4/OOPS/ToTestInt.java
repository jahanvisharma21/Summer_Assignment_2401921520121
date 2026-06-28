interface test {
    int square(int n);
}
class Arithmetic implements test {

    public int square(int n) {
        return n * n;
    }
}
public class ToTestInt {

    public static void main(String[] args) {

        Arithmetic obj = new Arithmetic();

        System.out.println("Square of 5 = " + obj.square(5));
        System.out.println("Square of 10 = " + obj.square(10));
    }
}
