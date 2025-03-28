namespace Simple
{
int user_input()
{
    return 42;
}

void sink(int x)
{
}

class Foo
{
    int a_;
    int b_;

public:
    int a() { return a_; }
    int b() { return b_; }
    void setA(int a) { a_ = a; }
    void setB(int b) { b_ = b; }

    Foo(int a, int b) : a_(a), b_(b){};
};

void bar(Foo &f)
{
    sink(f.a()); // $ ast=39:12 ast=41:12 ir=39:12 ir=41:12
    sink(f.b()); // $ ast=40:12 ast=42:12 ir=40:12 ir=42:12
}

void foo()
{
    Foo f(0, 0);
    Foo g(0, 0);
    Foo h(0, 0);
    Foo i(0, 0);

    f.setA(user_input());
    g.setB(user_input());
    h.setA(user_input());
    h.setB(user_input());

    // Only a() should alert
    bar(f);

    // Only b() should alert
    bar(g);

    // Both a() and b() should alert
    bar(h);

    // Nothing should alert
    bar(i);
}

struct A
{
    int i;
};

void single_field_test()
{
    A a;
    a.i = user_input();
    A a2 = a;
    sink(a2.i); //$ ast,ir
}

struct C {
    int f1;
};

struct C2
{
    C f2;

    int getf2f1() {
        return f2.f1;
    }

    void m() {
        f2.f1 = user_input();
        sink(getf2f1()); //$ ast,ir
    }
};

typedef A A_typedef;

void single_field_test_typedef(A_typedef a)
{
    a.i = user_input();
    A_typedef a2 = a;
    sink(a2.i); //$ ast,ir
}

namespace TestAdditionalCallTargets {

    using TakesIntReturnsVoid = void(*)(int);
    template<TakesIntReturnsVoid F>
    void call_template_argument(int);

    void call_sink(int x) {
        sink(x); // $ ir
    }

    void test_additional_call_targets() {
        int x = user_input();
        call_template_argument<call_sink>(x);
    }

}

void post_update_to_phi_input(bool b)
{
  A a;
  if(b) {
    a.i = user_input();
  }
  sink(a.i); // $ ast,ir
}

void write_to_param(int* p) {
    *p = user_input();
}

void alias_with_fields(bool b) {
    A a;
    int* q;
    if(b) {
        q = &a.i;
    } else {
        q = nullptr;
    }
    write_to_param(q);
    sink(a.i); // $ MISSING: ast,ir
}

} // namespace Simple