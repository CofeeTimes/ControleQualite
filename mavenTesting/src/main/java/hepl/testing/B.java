package hepl.testing;

public class B {
    private int y;

    public B(){
        y = 0;
    }

    public void doX(){
        System.out.println("doX");
    }

    public int doY(){
        return -1;
    }

    public int getY(){
        return y;
    }
}