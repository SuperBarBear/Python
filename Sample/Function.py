presidents = ["Washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Adams", "Jackson"]


for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
x = list(enumerate(seasons))
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
y = list(enumerate(seasons, start=3))       # 下标从 1 开始
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
print(x)

print(y)
