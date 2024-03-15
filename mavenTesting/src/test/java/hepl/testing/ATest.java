package hepl.testing;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;

import org.mockito.Mock;
import org.mockito.Mockito;
import static org.mockito.Mockito.*;
import org.mockito.runners.MockitoJUnitRunner;

@SuppressWarnings({ "deprecation", "unused" }) // If not problems with deprecated methods and unused variables
@RunWith(MockitoJUnitRunner.class)
public class ATest {
    A a;
    //@Mock
    B b;

    public ATest() {
    }
    
    @Before
    public void setUp() {
        b = mock(B.class);
        a = new A(b);
    }

    @After
    public void tearDown() {
    }

    @Test
    public void testCallDoX() {
        a.callDoX();
        verify(b).doX();
    }

    @Test
    public void testCallDoY() {
        when(b.getY()).thenReturn(-1);
        assertEquals(-2, a.callDoY());
    }
}