import java.util.Scanner;

public class ChooseYourOwnHomework {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Welcome to the Choose Your Own Design Pattern HW!\n");

		CalculationTemplate calculator;
		int input = 4;
		Scanner sysInput = new Scanner(System.in);

		while(input != 3)
		{
			System.out.println("Press 1 for reduced calculations, 2 for detailed, or 3 to exit");
			input = sysInput.nextInt();

			if(input == 1)
			{
				calculator = new ReducedCalculation("values");
				calculator.runCalculation();
			}
			else if(input == 2)
			{
				calculator = new DetailedCalculation("values");
				calculator.runCalculation();
			}
			else if(input != 3)
			{
				System.out.println("Invalid input");
			}

		}

	}

}
