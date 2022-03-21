jackalopes = [0, 0]
jackalope_population = 0
years = 0
# jackalopes_next = []

# for x in range(len(jackalopes)):
#     while jackalopes[x] < 10:
#             jackalopes[x] += 1
#     years += 1

# print(jackalopes)
# print(years)

# while True:
#     if len(jackalopes) >= 1000:
#         break
#     else:
#         for x in jackalopes:
#             if x == 0:
#                 x =1

def one_generation(generation):
        jackalopes_next = []
        for x in generation:
            if x == 0:
                jackalopes_next.append(1)
            elif x == 1:
                jackalopes_next.append(2)
            elif x == 2:
                jackalopes_next.append(3)
            elif x == 3:
                jackalopes_next.append(4)
            elif x == 4:
                jackalopes_next.append(5)
            elif x == 5:
                jackalopes_next.append(6)
            elif x == 6:
                jackalopes_next.append(7)
            elif x == 7:
                jackalopes_next.append(8)
            elif x == 8:
                jackalopes_next.append(9)
            elif x == 9:
                jackalopes_next.append(10)
        # Reproduction
        # for x in range(0, (generation.count(4) // 2)):
        #     jackalopes_next.append(0)
        # for x in range(0, (generation.count(5) // 2)):
        #     jackalopes_next.append(0)
        # for x in range(0, (generation.count(6) // 2)):
        #     jackalopes_next.append(0)
        # for x in range(0, (generation.count(7) // 2)):
        #     jackalopes_next.append(0)
        # for x in range(0, (generation.count(8) // 2)):
        #     jackalopes_next.append(0)
        fours = jackalopes_next.count(4)
        fives = jackalopes_next.count(5)
        sixes = jackalopes_next.count(6)
        sevens = jackalopes_next.count(7)
        eights = jackalopes_next.count(8)

        sum_adults = fours + fives + sixes + sevens + eights

        new_babies = sum_adults // 2

        for n in range(0, new_babies):
            jackalopes_next.append(0)
            jackalopes_next.append(0)
        
        return jackalopes_next

for year in range(0,10):
    jackalopes = one_generation(jackalopes)

print(jackalopes)

print(len(jackalopes))
