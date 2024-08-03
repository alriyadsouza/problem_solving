class Solution:
    @staticmethod
    def monster(exp, power, bonus):
        Zip = list(zip(power, bonus))
        sorted_zip = sorted(Zip, key=lambda x: x[0])
        count = 0
        for i, j in sorted_zip:
            if exp >= i:
                exp += j
                count += 1
        return count

# Input handling
n = int(input("Number of monsters: "))
exp = int(input("Initial experience: "))
power = []
bonus = []

print("Enter power for each monster:")
for i in range(n):
    power.append(int(input()))

print("Enter bonus for each monster:")
for i in range(n):
    bonus.append(int(input()))

solution = Solution()
result = solution.monster(exp, power, bonus)
print("Maximum number of monsters that can be defeated:", result)
