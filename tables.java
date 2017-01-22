import java.io.*;
import java.util.*;

class tables{
	public static void main(String args[])throws IOException{
		DataInputStream input = new DataInputStream(System.in);
		System.out.println("Are_you_Excited_Enter Num");
		int num= Integer.parseInt(input.readLine());
		System.out.println("Hello Lets Begin!");

		for(int i=1;i<=num;i++){
			for(int j=1;j<=10;j++){
				System.out.print(i+"x"+j+"= "+i*j);
				if(i<10){
					System.out.print(" ");
				}
				if(i*j<=9){
					System.out.print("   | ");
				}
				else if(i*j<=99){
					System.out.print("  | ");
				}
				else if(i*j<=999){
					System.out.print(" | ");
				}
				else{
					System.out.println("| ");
				}
			}
			System.out.println("");
		}
	}
}
