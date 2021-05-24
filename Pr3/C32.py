class C32:

    def __init__(self):
        self.state: C32.State = C32.A(self)

    def make(self) -> int:
        return self.state.make()

    def send(self) -> int:
        return self.state.send()

    def rush(self) -> int:
        return self.state.rush()

    class State:
        def __init__(self, parent):

            self.parent: C32 = parent

        def make(self) -> int:
            raise RuntimeError

        def send(self) -> int:
            raise RuntimeError

        def rush(self) -> int:
            raise RuntimeError

    class A(State):
        def make(self):
            self.parent.state = C32.B(self.parent)
            return 0

        def send(self):
            self.parent.state = C32.C(self.parent)
            return 1

    class B(State):
        def make(self):
            self.parent.state = C32.B(self.parent)
            return 4

        def send(self):
            self.parent.state = C32.C(self.parent)
            return 2

        def rush(self):
            self.parent.state = C32.D(self.parent)
            return 3

    class C(State):
        def rush(self):
            self.parent.state = C32.D(self.parent)
            return 5

    class D(State):
        def make(self):
            self.parent.state = C32.E(self.parent)
            return 6

    class E(State):
        def send(self):
            self.parent.state = C32.A(self.parent)
            return 8

        def rush(self):
            self.parent.state = C32.F(self.parent)
            return 7

    class F(State):
        pass
