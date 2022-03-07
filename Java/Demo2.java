import java.util.Scanner;
public class Demo2 {
	public static void main(String[] args) {
	
		int[] id = new int[5];
		//int x=200;
		for(int i=0;i<id.length;i++) {
			Scanner sc= new Scanner(System.in);
			
			id[i]= sc.nextInt();
			//x++;
			
		}
		for(int i:id)
			System.out.println(i);
		}
}
