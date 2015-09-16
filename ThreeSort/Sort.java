import java.util.Arrays;
import java.util.Scanner;

public class Sort { //class name is SOrt
	public void threeSort () { //Method is called threeSort
				
		Scanner num = new Scanner (System.in);
		
		int fnum = 0, snum = 0, tnum = 0; //initialize variables
				
		System.out.println ("Enter first num: ");
		fnum = num.nextInt(); //input for number. Method for string is .nextLine
		
		System.out.println ("Enter second num: ");
		snum = num.nextInt();	
		
		System.out.println ("Enter third num: ");
		tnum = num.nextInt();	
		
		int [] intArray = {fnum , snum , tnum}; //create an array of three integers
		
		//Print the unsorted Array	
		// Converts it from array to string then prints
		// %s - string \n creates new line
		System.out.printf("Unsorted array: %s\n", Arrays.toString(intArray));
		
		//Sort the array using the 'Arrays.sort' inbuilt method
		Arrays.sort(intArray);
		System.out.printf("Sorted array: %s\n", Arrays.toString(intArray));
	
	}
}