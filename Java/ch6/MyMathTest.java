public class MyMathTest {

	public static void main(String[] args) {
		MyMath mm;
		mm= new MyMath();
		long result1=mm.add(5L,3L);
		long result2=mm.substract(5L, 3L);
		long result3=mm.multiply(5L, 3L);
		double result4=mm.divide(5L, 3L);//long 타입 자동으로 형 변환
		System.out.println(result1);
		System.out.println(result2);
		System.out.println(result3);
		System.out.println(result4);
	}

}

class MyMath{
	long add(long a,long b) {
		return a+b;
	}
	long substract(long a,long b) {return a-b;}
	long multiply(long a, long b) {return a*b;}
	double divide(double a, double b) {return a/b;}
	
}
