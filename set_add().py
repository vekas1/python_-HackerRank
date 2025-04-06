# Enter your code here. Read input from STDIN. Print output to STDOUT
country_stamps = set()

n = int(input())

for _ in range(n):
    country = input()
    country_stamps.add(country)
    
print(len(country_stamps))
