1. #Többszörös beágyazások foor ciklusok
'''
Az ilyen többszörös (beágyazott) for ciklusokat olyan helyzetekben érdemes használni, amikor a feladat többszörös dimenziós adatok, struktúrák vagy kombinációk kezelését igényli. Ezek a ciklusok hasznosak olyan problémák megoldására, ahol az elemek, objektumok vagy változók kombinációi létrehoznak egy nagyobb struktúrát, amelyben az egyes dimenziók változhatnak, és egymással kombinálhatók.

Például érdemes használni:

1. 3D vagy többdimenziós rácsok kezelésére: Amikor több dimenziójú rácsot (pl. 3D térben vagy még magasabb dimenziókban) szeretnénk kezelni, a többszörös for ciklusok segítenek létrehozni és bejárni ezeket a rácsokat.

2. Matematikai kombinációk vagy permutációk létrehozására: Amikor az elemek kombinációit vagy permutációit kell létrehozni (például egy adott halmaz elemeiből), akkor többszörös for ciklusokkal hatékonyan generálhatjuk ezeket az összes lehetséges kombinációkat.

3. Keresés és összehasonlítás többszörös dimenziókban: Amikor több dimenziójú adatszerkezetekben keresünk vagy összehasonlítunk elemeket, akkor többszörös for ciklusokat használhatunk az elemek elérése és kezelése érdekében.

Azonban érdemes körültekintően használni a többszörös for ciklusokat, mert ezek a ciklusok növelhetik a futási időt, és ha túl mélyen vagy túl sokszor ágyazzuk be őket, akkor a kód olvashatósága jelentősen romolhat. Az ilyen esetekben más megközelítéseket is érdemes megfontolni, például list comprehension-t, rekurziót vagy más algoritmusokat, amelyek hatékonyabban kezelik az adott problémát.
'''
3.

# 2D mátrix létrehozása
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Keresett elem értéke
target = 5

# Többszörös for ciklusokkal keresünk a mátrixban
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            print(f"A {target} elem megtalálható a ({i}, {j}) pozícióban.")


# 3D rács létrehozása
grid = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Összehasonlított elem értéke
compare_element = [3, 4]

# Többszörös for ciklusokkal összehasonlítjuk az elemeket a rácsban
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == compare_element:
            print(f"Az összehasonlított elem megtalálható a ({i}, {j}) pozícióban.")

# 4D adattömb létrehozása
data = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

# Keresett adat értéke
target_data = [13, 14]

# Többszörös for ciklusokkal keresünk az adattömbben
for i in range(len(data)):
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            for l in range(len(data[i][j][k])):
                if data[i][j][k][l] == target_data:
                    print(f"A keresett adat megtalálható a ({i}, {j}, {k}, {l}) pozícióban.")
                    
2. 

from itertools import combinations

# Adott halmaz
my_set = [1, 2, 3, 4]

# Kombinációk létrehozása 2 elemű részhalmazokkal
combinations_2 = list(combinations(my_set, 2))
print(combinations_2)
# Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

from itertools import permutations

# Adott halmaz
my_set = [1, 2, 3]

# Permutációk létrehozása
permutations_3 = list(permutations(my_set))
print(permutations_3)
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# Adott szám
number = 123

# Az összes lehetséges számjegy kombinációk létrehozása
digits = [int(digit) for digit in str(number)]
combinations = []
for i in range(1, len(digits) + 1):
    combinations.extend(list(combinations(digits, i)))

print(combinations)
# Output: [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]


1. 

# 3D rács méretei
x_size = 3
y_size = 4
z_size = 2

# 3D rács létrehozása többszörös for ciklusokkal
grid = [[[0 for _ in range(z_size)] for _ in range(y_size)] for _ in range(x_size)]

# A rács feltöltése értékekkel
for x in range(x_size):
    for y in range(y_size):
        for z in range(z_size):
            grid[x][y][z] = x * y * z

# 3D rács kiíratása
for x in range(x_size):
    for y in range(y_size):
        for z in range(z_size):
            print(f"({x}, {y}, {z}): {grid[x][y][z]}")




