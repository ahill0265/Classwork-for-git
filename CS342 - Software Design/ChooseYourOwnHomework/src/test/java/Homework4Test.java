import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class Homework4Test {

    CalculationTemplate reduced;
    CalculationTemplate detailed;

    double[] reducedTest;
    double[] detailedTest;

    @Test
    void testReduced()
    {
        reduced = new ReducedCalculation("test");
        reduced.runCalculation();
        reducedTest = reduced.test();
        assertEquals(12.0, reducedTest[0], "reduced sum incorrect");
        assertEquals(3.0, reducedTest[1], "reduced mean incorrect");
        assertEquals(3.0, reducedTest[2], "reduced median incorrect");
    }

    @Test
    void testDetailed()
    {
        detailed = new DetailedCalculation("test");
        detailed.runCalculation();
        detailedTest = detailed.test();
        assertEquals(12.0, detailedTest[0], "detailed sum incorrect");
        assertEquals(3.0, detailedTest[1], "detailed mean incorrect");
        assertEquals(3.0, detailedTest[2], "detailed median incorrect");
        assertEquals( 1.0, detailedTest[3] , "detailed std incorrect");
        assertEquals( 2.0, detailedTest[4], "detailed mode incorrect");
        assertEquals( 4.0, detailedTest[5], "detailed max incorrect");
        assertEquals( 2.0, detailedTest[6], "detailed min incorrect";
    }

}
