public class Demo {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int x=0;
		int[] num = new int[3];
		
		while(x<args.length) {
			num[x]=Integer.parseInt(args[x]);
			System.out.println(num[x]);
			x++;
		}
		
	}
}
