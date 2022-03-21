import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import org.junit.jupiter.api.DisplayName;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class CoffeeDecoratorTest {

	Coffee order;

	@BeforeEach
	void init()
	{
		order = new BasicCoffee();
	}

	@Test
	void testInit()
	{
		assertEquals(3.99, order.makeCoffee(), "Basic coffee should be $3.99");
	}

	@Test
	void testDesignPattern()
	{
		order = new Cream(order);
		assertEquals(4.49, order.makeCoffee(), "Coffee + cream should be $4.49");
	}

	@Test
	void testFullOrderAtOnce()
	{
		order = new Cream(new ExtraShot(new Sugar(new Vanilla (new WhippedCream(order)))));
		assertEquals(8.19, Math.round(order.makeCoffee()*100.0)/100.0, "1 of everything should be $8.19");
	}

	@Test
	void testFullOrderOneAtATime()
	{
		assertEquals(3.99, order.makeCoffee(), "Base should be $3.99");

		order = new Cream(order);
		assertEquals(4.49, order.makeCoffee(), "+cream should be $4.49");

		order = new ExtraShot(order);
		assertEquals(5.69, order.makeCoffee(), "+cream, shot should be $5.69");

		order = new Sugar(order);
		assertEquals(6.19, order.makeCoffee(), "+cream, shot, sugar should be $6.19");

		order = new Vanilla(order);
		assertEquals(7.69, order.makeCoffee(), "+cream, shot, sugar, vanilla should be $7.69");

		order = new WhippedCream(order);
		assertEquals(8.19, Math.round(order.makeCoffee()*100.0)/100.0, "1 of everything should be $8.19");
	}

	@Test
	void testMultipleAdditions()
	{
		order = new Cream(order);
		order = new Cream(order);
		assertEquals(4.99, order.makeCoffee(), "Cream x2 should be $4.99");

		order = new Cream(new Cream(order));
		assertEquals(5.99, order.makeCoffee(), "cream x4 should be $5.99");
	}

	@Test
	void testOrderDoesNotMatter()
	{
		order = new Cream(new ExtraShot(order));
		assertEquals(5.69, order.makeCoffee(), "Cream+Shot should be $5.69");

		Coffee order2 = new BasicCoffee();
		order2 = new ExtraShot(new Cream(order2));
		assertEquals(5.69, order2.makeCoffee(), "Cream+Shot should be $5.69");
	}

}
