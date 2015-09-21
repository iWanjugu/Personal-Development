import java.util.Arrays;

public class SortThree {
	public static int[] threeSort (int num1, int num2, int num3) {
		//return type is an array of integers

		//MAX:
		int max = Math.max(num1, num2);
		//checks which one is greater between num1 and num2;
		//the higher value is stored in a variable called 'max'

		int maxfinal = 	Math.max(max, num3);
		//checks which one is greater between 'max, and num3;
		//the higher value is stored in a variable called 'maxfinal'


		//MIN:
		int min = Math.min(num1, num2);
		int minfinal = 	Math.min(min, num3);

		//MID:
		int mid = (num1 + num2 + num3) - minfinal - maxfinal;


		int [] result = {minfinal, mid, maxfinal};
		return result;

	}
		public static void main (String args []){
			int [] result = threeSort (25,47,6);
		}


	}

}
