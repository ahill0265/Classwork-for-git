public class Vanilla extends CoffeeDecorator
{
    private double cost = 1.50;

    Vanilla(Coffee specialCoffee)
    {
        super(specialCoffee);
    }

    public double makeCoffee()
    {
        return specialCoffee.makeCoffee() + addVanilla();
    }

    private double addVanilla()
    {
        System.out.println(" + vanilla: $1.50");
        return cost;
    }

}
