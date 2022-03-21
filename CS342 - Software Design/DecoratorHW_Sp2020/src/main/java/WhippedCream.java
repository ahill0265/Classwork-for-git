public class WhippedCream extends CoffeeDecorator {

    private double cost = .50;

    WhippedCream(Coffee specialCoffee)
    {
        super(specialCoffee);
    }

    public double makeCoffee()
    {
        return specialCoffee.makeCoffee() + addWhippedCream();
    }

    private double addWhippedCream()
    {
        System.out.println(" + whipped cream: $.50");
        return cost;
    }
}
