interface Printable{
    void print();
    int MAX_COUNT=10;
}
class MyClass implements Printable{
    public void print(){
        System.out.println("123");
    }
}
public class test {
    public static void main(String[] args){
        MyClass my=new MyClass();
        my.print();
        System.out.println("Max count="+Printable.MAX_COUNT);
    }
}
