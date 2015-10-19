// Using java, have the function divide(num1,num2)
// take both parameters being passed and return the Greatest Common Factor.
// That is, return the greatest number that evenly goes into both numbers with no remainder.
// For example: 20 and 10 both are divisible by 1, 2, 5 and 10 so the output should be 10.
// The range for both parameters will be from 1 to 10^3.

import java.util.Scanner;

public class GCF {
	private static int divide(int num1, int num2)  {
		// TODO Auto-generated method stub
		int c = 0, cf = 0, i = 1;
		c = Math.min(num1, num2);

		for (i=1; i <= c+1; i++)
    	{
    		if (num1%i==0 && num2%i==0 )
    		{
              cf = i;
    		}
    	}
    	return cf;
	}

    public static void main (String args []){
    	Scanner num = new Scanner (System.in);

		int num1 = 0, num2 = 0;
		System.out.println ("Enter first num: ");
		num1 = num.nextInt(); //input for number. Method for string

		System.out.println ("Enter second num: ");
		num2 = num.nextInt();

    	int cf = divide(num1, num2);
    	System.out.println (cf);
    }
}

