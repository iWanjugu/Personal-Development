// Using java solve the problem below:
// Given an array of integers, find the maximum and minimum of this array.

import java.util.*;
//import java.util.Arrays;
//import java.util.Scanner;
//import java.util.Collections;


public class maximum_and_minimum {
	public static String[] minmax(int[]arr) {

		int min = 0, max = 0;
		Arrays.sort(arr);

		min = arr[0]; //First item = min
		max = arr[arr.length-1]; //Last item = max

		String maximum = ("Maximum Value is: " +max);
		String minimum = ("Minimum Value is: " +min);

		String [] result = {maximum, minimum};
		return result;
	}

			public static void main (String [] args) {
			Scanner num = new Scanner (System.in);
			int a=0, b=0, c=0, d=0;

			System.out.print("Enter numbers for the array: ");
			a = num.nextInt();
			b = num.nextInt();
			c = num.nextInt();
			d = num.nextInt();

			int [] arr = new int [] {a, b, c, d};
			// Printing ARRAYS
			// System.out.print(Arrays.toString(arr));

			// Results
			String [] result= minmax(arr);
			System.out.print(Arrays.toString(result));


	}
}
