// Using JAVA, answer the question below:
// Reverse the words in a given sentence.
// Words are always delimited by spaces.
// For example if the given word is "reverse words of a sentence".
// The output will be "sentence a of words reverse"

import java.util.*;

public class reverse_words {
	public static void main (String [] args){

		String str = new String("bad boy");
		String[]str_ = str.split(" ");
//		System.out.println(str_[0]);
//		System.out.println(str_[1]);
//		System.out.println(str_.length);

		String str_rev = "";

		int len = str_.length;
		Range rev_num = new Range(len, 0);

		for (int i=(str_.length-1);i<1; i--) {
			str_rev = str_rev + " " + str_[i];
			System.out.println(str_rev);
		}
	}
}