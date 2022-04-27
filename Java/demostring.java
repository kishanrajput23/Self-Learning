package string;
public class demostring {
	public static void main(String[]args) {
		
		//s1,s2 stores in same memory of parijoy
		String s1 = "Parijoy";
		String s2 = "Parijoy";
		
		//s3,s4 stores in different memory from parijoy
		String s3 = new String("Parijoy");
		String s4 = new String ("Parijoy");
		
		
		// "==" compare addresses
		if(s1==s2) {
			System.out.println("equal");
		}
		else
			System.out.println("not equal");
		
		if(s3==s4) {
			System.out.println("equal");
		}
		else
			System.out.println("not equal");
		
		// ".equals" compare real value of both
		if(s3.equals(s4)) {
			System.out.println("equal");
		}
		else
			System.out.println("not equal");
		
	
	
	
	}
}
