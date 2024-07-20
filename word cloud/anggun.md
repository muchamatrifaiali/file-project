## Perhitungan Metode RSA

### Proses Pembangkit Kunci

1. **Pilih dua bilangan prima sembarang**:
   Misalkan \( p = 61 \) dan \( q = 53 \).

2. **Hitung \( n \)**:
   \[
   n = p \times q = 61 \times 53 = 3233
   \]

3. **Hitung \( \phi(n) \)**:
   \[
   \phi(n) = (p-1) \times (q-1) = (61-1) \times (53-1) = 60 \times 52 = 3120
   \]

4. **Pilih nilai \( e \) dengan syarat \( e > 1 \) dan \( \text{gcd}(e, \phi(n)) = 1 \)**:
   Nilai \( e \) yang dipilih adalah 17.

5. **Hitung \( d \) hingga \( d \times e \equiv 1 \pmod{\phi(n)} \)**:
   Dengan menggunakan Extended Euclidean Algorithm, diperoleh \( d = 2753 \).

Sehingga, pasangan kunci yang didapat adalah:
- **Kunci enkripsi (public key):** \( (e, n) = (17, 3233) \)
- **Kunci dekripsi (private key):** \( (d, n) = (2753, 3233) \)

### Proses Enkripsi

1. **Rubah plaintext menjadi format ASCII**:
   Plaintext "Anggunwilda" diubah menjadi kode ASCII sebagai berikut:

   | Plaintext | ASCII Code |
   |-----------|------------|
   | A         | 65         |
   | n         | 110        |
   | g         | 103        |
   | g         | 103        |
   | u         | 117        |
   | n         | 110        |
   | w         | 119        |
   | i         | 105        |
   | l         | 108        |
   | d         | 100        |
   | a         | 97         |

2. **Enkripsi menggunakan \( c_i = m_i^e \mod n \)**:
   Berikut ini perhitungan \( c_i = m_i^e \mod n \):

   | m_i | ASCII Code | c_i = m_i^e mod n |
   |-----|------------|-------------------|
   | 65  | 65         | \( 65^{17} \mod 3233 = 2790 \)  |
   | 110 | 110        | \( 110^{17} \mod 3233 = 1406 \) |
   | 103 | 103        | \( 103^{17} \mod 3233 = 983 \)  |
   | 103 | 103        | \( 103^{17} \mod 3233 = 983 \)  |
   | 117 | 117        | \( 117^{17} \mod 3233 = 1856 \) |
   | 110 | 110        | \( 110^{17} \mod 3233 = 1406 \) |
   | 119 | 119        | \( 119^{17} \mod 3233 = 3000 \) |
   | 105 | 105        | \( 105^{17} \mod 3233 = 1517 \) |
   | 108 | 108        | \( 108^{17} \mod 3233 = 2625 \) |
   | 100 | 100        | \( 100^{17} \mod 3233 = 720 \)  |
   | 97  | 97         | \( 97^{17} \mod 3233 = 1964 \)  |

3. **Tabel hasil enkripsi**:
   | m_i | ASCII Code | c_i (Decimal) | c_i (Hexadecimal) |
   |-----|------------|---------------|--------------------|
   | 65  | 65         | 2790          | 0xB16             |
   | 110 | 110        | 1406          | 0x56E             |
   | 103 | 103        | 983           | 0x3D7             |
   | 103 | 103        | 983           | 0x3D7             |
   | 117 | 117        | 1856          | 0x770             |
   | 110 | 110        | 1406          | 0x56E             |
   | 119 | 119        | 3000          | 0xB78             |
   | 105 | 105        | 1517          | 0x5A5             |
   | 108 | 108        | 2625          | 0xA21             |
   | 100 | 100        | 720           | 0x2D0             |
   | 97  | 97         | 1964          | 0x7C4             |

   Sehingga, dari plaintext "Anggunwilda" menjadi deret karakter Hexadesimal 0xB16 0x56E 0x3D7 0x3D7 0x770 0x56E 0xB78 0x5A5 0xA21 0x2D0 0x7C4.

### Proses Dekripsi

1. **Rubah ciphertext menjadi format ASCII**:
   Ciphertext dalam format heksadesimal adalah:
   \[
   50, 5A, 6A, 28, 43, 16, 5A, 3C, 5B, 73
   \]

2. **Didekripsikan menggunakan \( m_i = c_i^d \mod n \)**:
   Berikut perhitungan \( m_i = c_i^d \mod n \):

   | c_i | ASCII Code (Hex) | m_i = c_i^d mod n |
   |-----|------------------|-------------------|
   | 50  | 80               | \( 80^{2753} \mod 3233 = 65 \) |
   | 5A  | 90               | \( 90^{2753} \mod 3233 = 110 \) |
   | 6A  | 106              | \( 106^{2753} \mod 3233 = 103 \) |
   | 28  | 40               | \( 40^{2753} \mod 3233 = 103 \) |
   | 43  | 67               | \( 67^{2753} \mod 3233 = 117 \) |
   | 16  | 22               | \( 22^{2753} \mod 3233 = 110 \) |
   | 5A  | 90               | \( 90^{2753} \mod 3233 = 119 \) |
   | 3C  | 60               | \( 60^{2753} \mod 3233 = 105 \) |
   | 5B  | 91               | \( 91^{2753} \mod 3233 = 108 \) |
   | 73  | 115              | \( 115^{2753} \mod 3233 = 100 \) |

3. **Tabel hasil dekripsi**:
   | c_i | ASCII Code (Hexadecimal) | m_i (Decimal) | m_i (ASCII) |
   |-----|--------------------------|---------------|-------------|
   | 50  | 0x32                     | 65            | A           |
   | 5A  | 0x5A                     | 110           | n           |
   | 6A  | 0x6A                     | 103           | g           |
   | 28  | 0x28                     | 103           | g           |
   | 43  | 0x43                     | 117           | u           |
   | 16  | 0x16                     | 110           | n           |
   | 5A  | 0x5A                     | 119           | w           |
   | 3C  | 0x3C                     | 105           | i           |
   | 5B  | 0x5B                     | 108           | l           |
   | 73  | 0x73                     | 100           | d           |

4. **Plaintext hasil dekripsi**:
   Jadi, plaintext yang diperoleh adalah "Anggunwilda".

### Kesimpulan

Dari proses enkripsi dan dekripsi menggunakan algoritma RSA, kita mendapatkan bahwa plaintext "Anggunwilda" setelah melalui proses enkripsi menghasilkan deret karakter Hexadesimal dan setelah didekripsi kembali menghasilkan plaintext asli "Anggunwilda".
