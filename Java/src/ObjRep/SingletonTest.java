package ObjRep;

/**
 * Singleton pattern uses a private constructor paired with a getInstance() method.
 * If the instance doesn't exist, the constructor is called and object is returned.
 * If it does exist, nothing happens. Since the object is static, only one
 * is allowed to exist at a time.
 */
public class SingletonTest {
    public static void main(String[] args)  {
        Singleton s1 = Singleton.get_instance();
        s1.seti(4);
        System.out.println(s1.geti());
        //Singleton s2 = new Singleton(); Illegal
    }
}

class Singleton {
    private static int i;
    private static Singleton _instance = null;

    private Singleton() {
    }

    public static Singleton get_instance() {
        if (_instance == null) {
            _instance = new Singleton();
        }
        return _instance;
    }

    public int geti() {
        return i;
    }

    public void seti(int i) {
        this.i = i;
    }
}
