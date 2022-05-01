class InstanceofTest {
    public static void main(String[] args) {
        // Enter Your Code Here
        FireEngine fe = new FireEngine();

        if (fe instanceof FireEngine){
            System.out.println("This is a FireEngine instance.");
        }
        if (fe instanceof Car) {
            System.out.println("This is a Car instance.");
        }
        if (fe instanceof Object){
            System.out.println("This is a Object instance.");
        }

    }
}

class Car {}
class FireEngine extends Car {}
