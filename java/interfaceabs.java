import java.util.Scanner;
public interface interfaceabs {
    
        void getArea(int length, int breadth);
}

// implement the Polygon interface
class Rectangle implements interfaceabs {
        // implementation of abstract method
        
        public void getArea(int length, int breadth) {
        System.out.println("The area of the rectangle is " + (length * breadth));
}
}
class Main {
public static void main(String[] args) {
Rectangle r1 = new Rectangle();
Scanner s1=new Scanner(System.in);
System.out.println("Enter length and breadth :- ");
r1.getArea(s1.nextInt(),s1.nextInt());
s1.close();
}
}