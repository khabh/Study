class FighterTest {
    public static void main(String[] args) {
        // Enter Your Code Here
        Fighter f = new Fighter();
        if (f instanceof Unit)
            System.out.println("f는 Unit 클래스의 자손입니다.");
        if (f instanceof Fightable)
            System.out.println("f는 movable 인터페이스를 구현했습니다.");
        if (f instanceof Movable)
            System.out.println("f는 Attackable인터페이스를 구현했습니다.");
        if (f instanceof Object)
            System.out.println("f는 Object클래스의 자손입니다.");
    }
}

class Unit {
    int currentHP;
    int x;
    int y;
}

interface Movable { void move(int x, int y);}
interface Attackable { void attack(Unit u);}
interface Fightable extends Movable, Attackable {}

class Fighter extends Unit implements Fightable {
    public void move(int x, int y) {/* */} //오버라이딩 시 조상의 메서드보다 넓은 범위의 접근 제어자를 지정해야 한다 (인터페이스의 메서드는 public abstract)
    public void attack(Unit u){ /* */}
}