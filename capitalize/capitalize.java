// Using java, have the function capitalize(str) take the str parameter being passed and capitalize 
// the first letter of each word. Words will be separated by only one space. 
// the scanner object should be in the main method, from where we are going to call our function for testing
// it should take string input from a user


import java.util.Scanner;
import java.util.Arrays;

class Capitalize
{
	public static String capitalize (String str)
	{
		String [] word = str.split(" "); //split this string (according to where spaces are) and put it in an array
		StringBuilder Sb = new StringBuilder(); //creating an object of CLASS StringBuilder; StringBuffer can be used instead

		for (int i = 0; i < word.length; i++) {

			Sb.append(Character.toUpperCase(word[i].charAt(0))).append(word[i].substring(1)).append(" ");

		//word[i] - ith element of the word array
		//charAt(0) - first character of the ith element of the array
		//.substring(1) - takes the rest of the letters from point 1 e.g cake.substring(1) = "ake"

		}

		return Sb.toString().trim(); //convert the appended string
	}
	public static void main (String args [])
	{
		Scanner input = new Scanner (System.in);

		System.out.println ("Input a sentence: ");

		String sentence = input.nextLine();
		System.out.println (capitalize(sentence));

	}

}
