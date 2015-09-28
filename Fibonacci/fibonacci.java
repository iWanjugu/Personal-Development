// Using java, write a program that prints out the numbers in the Fibonacci series
// between 1 and 50 i.e.
// The first ten Fibonacci numbers are:
// ```
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
// ```
// The logic behind is that each subsequent number is the sum of the previous two i.e
// 0,1 are the first two, then 1,1 are the next then 1,2 follows e.t.c


public class fibonacci {
		//create variable
		static int x = 0, y = 1;
		static int f_sum()
		{
			// now we loop
			for (x = 0; x+x < 50; x++ )
			{
				x = x+y;
				y = x;
				System.out.print(x + " ");
			}
			return x;
		}
	public static void main (String args [])
		{
		System.out.print(f_sum());
	}
}
