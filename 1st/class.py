def main():
    x = Astronomy("김태현", 100)
    print(x.name)
    print(x.score)
    print(x.percent())

class Astronomy:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def percent(self):
        return self.score / 100

if __name__ == "__main__":
    main()
