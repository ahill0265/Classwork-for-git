import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class ReducedCalculation extends CalculationTemplate
{
    double sum;
    double mean;
    double median;

    private double[] values;

    ReducedCalculation(String filename)
    {
        values = new double[35];
        readInValues(filename);
    }

    //I took this code from homework 1
    private void readInValues(String filename) {

        try {
            File f = new File("src/main/resources/"+filename);

            Scanner s = new Scanner(f);

            int i = 0;
            while(s.hasNextDouble()) {
                values[i] = s.nextDouble();
                i++;
            }

            s.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

    public void calculate()
    {
        sum = sum();
        mean = mean();
        median = median();
    }

    public void displayData()
    {
        System.out.println("Statistics At A Glance");
        System.out.println("Sum: " + sum);
        System.out.println("Mean: " + mean);
        System.out.println("Median: " + median);
    }

    private double sum()
    {
        double sum = 0.0;

        for(double d: values)
        {
            sum += d;
        }

        return sum;
    }

    private double mean()
    {
        return(Arrays.stream(values).average().orElse(Double.NaN));
    }

    private double median()
    {
        boolean isOdd = ( values.length%2 == 1 );
        int length = values.length;

        if(isOdd)
        {
            return values[length/2];
        }
        else
        {
            double sum = values[length/2 - 1] + values[length/2];
            double result = sum/2.0;

            return result;
        }
    }

    public double[] test()
    {
        double[] testArray = new double[3];

        testArray[0] = sum;
        testArray[1] = mean;
        testArray[2] = median;

        return testArray;
    }

}
