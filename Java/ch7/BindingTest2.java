// class BindingTest2 {
//     public static void main(String[] args) {
//         // Enter Your Code Here

//         Parent parent = new Child();
//         Child child = new Child();

//         System.out.println("parent.x = " + parent.x);
//         parent.method();
//         System.out.println();
//         System.out.println("child.x = " + child.x);
//         child.method();
//     }   
// }

// class Parent {
//     int x = 100;

//     void method() {
//         System.out.println("Parent Method");
//     }
// }

// class Child extends Parent {
//     int x = 200;

//     void method () {
//         System.out.println("x = "+ x);
//         System.out.println("super.x = " + super.x);
//         System.out.println("this.x = " + this.x);
//     }
// }