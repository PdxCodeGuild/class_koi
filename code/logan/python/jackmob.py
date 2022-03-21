jackalopes = [0, 0]
# jackalopes_next =[]

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
            elif x == 6:
                jackalopes_next.append(7)
            elif x == 7:
                jackalopes_next.append(8)
            elif x == 8:
                jackalopes_next.append(9)
            elif x == 9:
                jackalopes_next.append(10)
        # Reproduction
        for x in range (0, (generation.count(4) // 2)):
            jackalopes_next.append(0)
        for x in range (0, (generation.count(5) // 2)):
            jackalopes_next.append(0)
        for x in range (0, (generation.count(6) // 2)):
            jackalopes_next.append(0)
        for x in range (0, (generation.count(7) // 2)):
            jackalopes_next.append(0)
        for x in range (0, (generation.count(8) // 2)):
            jackalopes_next.append(0)
        return jackalopes_next

for x in range (0,3):
    total = one_generation(jackalopes)

print(total)













# for x in jackalopes:
# # Handles aging
#     if x == 0:
#         jackalopes_next.append(1)
#     elif x == 1:
#         jackalopes_next.append(2)
#     elif x == 2:
#         jackalopes_next.append(3)
#     elif x == 3:
#         jackalopes_next.append(4)
#     elif x == 4:
#         jackalopes_next.append(5)
#     elif x == 5:
#         jackalopes_next.append(6)
#     elif x == 6:
#         jackalopes_next.append(7)
#     elif x == 6:
#         jackalopes_next.append(7)
#     elif x == 7:
#         jackalopes_next.append(8)
#     elif x == 8:
#         jackalopes_next.append(9)
#     elif x == 9:
#         jackalopes_next.append(10)
# # Reproduction
# for x in range (0, (jackalopes.count(4) // 2)):
#     jackalopes_next.append(0)
# for x in range (0, (jackalopes.count(5) // 2)):
#     jackalopes_next.append(0)
# for x in range (0, (jackalopes.count(6) // 2)):
#     jackalopes_next.append(0)
# for x in range (0, (jackalopes.count(7) // 2)):
#     jackalopes_next.append(0)
# for x in range (0, (jackalopes.count(8) // 2)):
#     jackalopes_next.append(0)


# jackalopes_next.append((jackalopes.count(4) // 2))
# jackalopes_next.append((jackalopes.count(5) // 2))
# jackalopes_next.append((jackalopes.count(6) // 2))
# jackalopes_next.append((jackalopes.count(7) // 2))
# jackalopes_next.append((jackalopes.count(8) // 2))



# print(jackalopes_next)