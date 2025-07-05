import java.util.Scanner;
import java.util.Random;

public class rock_paper_scissor_gme {
    public static void main(String[] args) {

        Scanner ab = new Scanner(System.in);
        System.out.println("Enter your choice : \n 0 for  ROCK \n 1 for " +
                "PAPER \n 2 for SCISSOR ");
        int userInput = ab.nextInt();

        Random random = new Random();
        int ComputerInput = random.nextInt(3);

        if (userInput==ComputerInput){
            System.out.println("Its a DRAW");
        } else if (userInput==0 && ComputerInput==2 || userInput==1&&ComputerInput==0 ||userInput==2&&ComputerInput==1) {
            System.out.println("YOU WON");

        }
        else
        {
            System.out.println("COMPUTER WON");
        }

        if (ComputerInput==0)
        {
            System.out.println("Computer choice:Rock");

        } else if (ComputerInput==1) {

            System.out.println("Computer choice:Paper");

        }
        else if(ComputerInput==2)
            System.out.println("Computer choice: Scissors");
    }
    }

