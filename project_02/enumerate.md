Fungsi `enumerate()` dalam Python digunakan untuk mengiterasi melalui elemen-elemen dalam sebuah objek yang dapat diiterasi (seperti list, tuple, atau string) sambil memberikan indeks posisi dari setiap elemen. Dengan kata lain, `enumerate()` tidak hanya memberi elemen dari objek yang diiterasi, tetapi juga indeksnya.

### Sintaks `enumerate()`
```python
enumerate(iterable, start=0)
```
- `iterable`: Objek yang dapat diiterasi (seperti list, tuple, string).
- `start`: Indeks awal (default adalah 0).

`enumerate()` mengembalikan objek enumerasi, yang dapat diubah menjadi list atau langsung digunakan dalam loop.

### Contoh Penggunaan `enumerate()`

#### Contoh 1: Iterasi dengan Indeks
Tanpa `enumerate()`, kamu hanya mengiterasi elemen:
```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

Dengan `enumerate()`, kamu juga mendapatkan indeks setiap elemen:
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```
Output:
```
0 apple
1 banana
2 cherry
```

#### Contoh 2: Menentukan Indeks Awal
Kamu bisa mengubah indeks awal dari 0 menjadi nilai lain dengan menambahkan argumen `start`:
```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```
Output:
```
1 apple
2 banana
3 cherry
```

#### Contoh 3: Menggunakan `enumerate()` untuk Modifikasi List
Misalkan kamu ingin menambahkan nomor urut di depan setiap elemen dalam list:
```python
names = ['John', 'Jane', 'Doe']
names_with_numbers = []

for i, name in enumerate(names, start=1):
    names_with_numbers.append(f"{i}. {name}")

print(names_with_numbers)
```
Output:
```
['1. John', '2. Jane', '3. Doe']
```

#### Contoh 4: Penggunaan di dalam List Comprehension
Kamu juga bisa menggunakan `enumerate()` di dalam list comprehension:
```python
fruits = ['apple', 'banana', 'cherry']
numbered_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(numbered_fruits)
```
Output:
```
['0: apple', '1: banana', '2: cherry']
```

### Kapan Menggunakan `enumerate()`?
- **Saat kamu butuh indeks elemen dalam iterasi:** Jika kamu perlu tahu indeks elemen saat melakukan iterasi, `enumerate()` adalah cara yang tepat.
- **Pengganti `range(len(...))`:** Tanpa `enumerate()`, kamu mungkin menggunakan `range(len())` untuk mendapatkan indeks, namun `enumerate()` lebih rapi dan langsung.

Contoh tanpa `enumerate()`:
```python
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, fruits[i])
```

Outputnya sama, tetapi `enumerate()` membuat kode lebih bersih dan lebih mudah dibaca.
"""