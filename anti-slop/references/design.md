# Anti-slop: desain (UI, web, grafis)

## Tanda slop desain

**Tipografi**
- Hanya Inter/Roboto/Arial/system-ui untuk semuanya, tanpa alasan.
- Satu ukuran dan bobot untuk hampir semua teks; hierarki hanya dari `font-bold`.
- Judul hero 3 baris dengan satu kata digradien.

**Warna**
- Gradien ungu-biru atau ungu-pink di hero, tombol, dan teks.
- Palet 5 warna yang "sama kuat" tanpa warna dominan.
- Mode gelap neon (cyan/magenta di atas hitam) sebagai satu-satunya gaya "modern".
- Kontras teks di bawah 4.5:1 (abu muda di atas putih).

**Layout dan komponen**
- Susunan baku: hero tengah, tiga kartu fitur sejajar dengan ikon, testimoni, harga tiga kolom, CTA, footer.
- Semua kartu: `rounded-2xl`, `shadow-lg`, border tipis, padding sama.
- Glassmorphism, blur, dan blob gradien dekoratif di mana-mana.
- Emoji sebagai ikon fitur; ikon berbeda gaya (outline dicampur solid).
- Bento grid tanpa hubungan antara ukuran sel dan pentingnya isi.
- Semua rata tengah; tidak ada ketegangan, asimetri, atau ruang kosong yang disengaja.

**Isi**
- Lorem ipsum, "Feature One", "John Doe", foto stok senyum, logo klien palsu.
- Statistik karangan ("99.9% uptime", "10K+ pengguna") dan testimoni tanpa sumber.
- Copy generik: "Revolusikan alur kerja Anda", "Solusi all-in-one".

**Interaksi dan kelengkapan**
- Hanya satu keadaan (default). Tidak ada hover, fokus, aktif, nonaktif, memuat, kosong, galat.
- Animasi `fade-in-up` pada semua elemen saat scroll; hover yang hanya `scale-105`.
- Tidak responsif, atau hanya "menumpuk jadi satu kolom".

## Cara menghindarinya

1. **Pilih arah dengan nama.** Contoh: "editorial majalah cetak", "panel instrumen industri", "kertas lab hangat", "brutalis monokrom". Arah yang baik berkonsekuensi pada font, grid, warna, ritme jarak, dan nada copy. Pilih yang cocok dengan audiens, bukan yang paling mencolok.
2. **Tetapkan token dulu**, lalu pakai konsisten: 1 warna aksen utama + netral bertingkat, skala jarak (kelipatan 4/8), skala tipografi dengan rasio jelas, 1-2 keluarga font (display + isi), radius seragam sesuai arah.
3. **Hierarki lewat kontras nyata**: ukuran, bobot, warna, ruang. Satu hal terbesar per layar. Jika semuanya menonjol, tidak ada yang menonjol.
4. **Layout mengikuti isi.** Mulai dari apa yang pengguna perlu lakukan atau lihat, baru tentukan grid. Pecah pola baku bila ada alasan: tabel padat untuk data, satu kolom lebar baca untuk teks panjang, split layout untuk perbandingan.
5. **Isi nyata.** Kalau belum ada konten dari user, tulis konten masuk akal yang spesifik pada domainnya dan tandai sebagai contoh. Jangan memajang angka karangan sebagai fakta.
6. **Lengkapi keadaan**: hover, `:focus-visible`, disabled, loading, kosong, galat, sukses untuk setiap elemen interaktif.
7. **Gerak punya tugas**: menjelaskan perubahan, memberi umpan balik, atau mengarahkan mata. Satu momen masuk yang dirancang baik lebih bernilai daripada sepuluh animasi acak. Hormati `prefers-reduced-motion`.
8. **Aksesibilitas dasar**: kontras 4.5:1 untuk teks isi, target sentuh minimal ~44px, label pada input, urutan fokus logis, `alt` bermakna, jangan mengandalkan warna saja.
9. **Responsif dengan sengaja**: rancang ulang susunan di layar sempit (urutan, ukuran teks, navigasi), bukan sekadar menumpuk.

## Uji cepat

- Tutup logo dan teks. Apakah halaman masih terasa milik merek ini, atau bisa milik ribuan situs lain?
- Sebut alasan untuk font, warna aksen, dan radius. Kalau jawabannya "karena umum", ganti.
- Adakah elemen yang bisa dihapus tanpa kehilangan informasi?
- Apakah tiap tombol dan input punya semua keadaannya?
