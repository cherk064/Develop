class Solution:
    def Name(self, name = "Ivan", lastname = "Ivanov", old = "14"):
        print("Hello ", name," ", lastname, " ", old, " years old")
a=Solution()
a.Name()
a.Name("Pasha")
a.Name("Pasha", "Ivanov")
a.Name("Pasha", "Ivanov", "15")