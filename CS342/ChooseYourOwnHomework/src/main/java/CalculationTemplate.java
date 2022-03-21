public abstract class CalculationTemplate
{
    public final void runCalculation()
    {
        calculate();
        displayData();
    }

    public abstract void calculate();
    public abstract void displayData();
    public abstract double[] test();
}
