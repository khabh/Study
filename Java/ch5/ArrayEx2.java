public class ArrayEx2 {

	public static void main(String[] args) {
		int[] arr = {10.9.8.7.3};
		int[] tmp= new int[arr.length*2];
		
		for(int i =0; i<arr.length;i++)
		{
			tmp[i]=arr[i];
		}
		arr=tmp;//참조변수 arr이 새로운 배열을 가리키게 한다.
		

	}

}
