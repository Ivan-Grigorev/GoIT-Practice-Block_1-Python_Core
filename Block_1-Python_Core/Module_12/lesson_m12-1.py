import pickle


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.p = open("myfile.txt", "w")

    def greet(self):
        print(f"Hello I'm {self.name}")

    def __getstate__(self):
        fields = self.__dict__.copy()
        fields.pop("p")
        return fields

    def __setstate__(self, state):
        self.__dict__ = state
        self.__dict__["p"] = None


def main():
    bob = Human("Bob", 25)
    with open("bob.dat", "wb") as f:
        pickle.dump(bob, f)

    with open("bob.dat", "rb") as f:
        bob = pickle.load(f)
        bob.greet()


if __name__ == "__main__":
    main()

#################################
