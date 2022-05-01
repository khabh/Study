// class PointTest {
//     public static void main(String[] args) {
//         // Enter Your Code Here
//         Point3D p3 = new Point3D(1, 2, 3);
//     }
// }

// class Point {
//     int x, y;

//     Point(int x, int y) {
//         this.x = x;
//         this.y = y;
    
//     }

//     String getLocaton() {
//         return "x :" + x + ", y : "+ y;
//     }
// }

// class Point3D extends Point {
//     int z;

//     // Point3D(int x, int y, int z) { 
//     //     // Implicit super constructor Point() is undefined. Must explicitly invoke another constructor
//     //  Point3D  클래스의 생성자의 첫 줄이 (조상의 것이든 자신의 것이든) 생성자를 호출하는 문장이 아니기 때문에 
//     //  컴파일러가 자동적으로 super(); 를 첫 줄에 추가한다
//     //  이때 조상 클래스에 Point()가 정의되어 있지 않기 때문에 에러가 발생한다.
//     //     this.x = x;
//     //     this.y = y;
//     //     this.z = z;
//     // }

//     Point3D(int x, int y, int z) { 
//         super(x,y);
//         this.x = x;
//         this.y = y;
//         this.z = z;
//     }

//     String getLocation() {
//         return "x :" + x + ", y : "+ y + ", z : " + z;
//     }
// }