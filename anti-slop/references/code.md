# Anti-slop: kode

## Tanda slop kode

**Fabrikasi dan klaim palsu**
- Memakai fungsi, flag CLI, atau package yang tidak ada (halusinasi API), atau versi yang salah.
- Menyatakan "sudah dites", "berjalan baik", atau "bug sudah diperbaiki" tanpa menjalankan apa pun.
- Implementasi pura-pura: `// TODO: implement`, fungsi yang mengembalikan data tiruan, `pass`, `return true`, tanpa memberi tahu user.
- Tes yang selalu lulus (meng-assert mock itu sendiri, atau `expect(true)`).

**Kelebihan struktur**
- Abstraksi untuk satu pemakaian: `Factory`, `Manager`, `Helper`, `Utils` yang membungkus satu panggilan.
- Konfigurasi, flag, dan parameter untuk kebutuhan yang belum ada.
- Dependensi baru untuk pekerjaan yang cukup dengan pustaka standar atau lima baris kode.
- Wrapper atas wrapper, event bus untuk dua fungsi.

**Kebisingan**
- Komentar yang mengulang kode (`// increment i`), docstring boilerplate di setiap fungsi, banner `// ===== Helper functions =====`.
- Nama generik: `data`, `result`, `temp`, `handleStuff`, `processData`, `item2`.
- Kode mati, impor tak terpakai, `console.log`/`print` debugging yang tertinggal.
- Pesan commit dan PR seperti "Update code" atau "Improve things".

**Penanganan galat yang buruk**
- `try/catch` yang menelan galat (`catch {}` atau hanya `console.log(e)`), lalu mengembalikan nilai default seolah sukses.
- Validasi di mana-mana tetapi tidak di batas sistem (input pengguna, jaringan, berkas).
- Fallback diam-diam yang menyembunyikan bug.

**Tidak menyatu dengan proyek**
- Gaya, penamaan, struktur folder, dan pola berbeda dari kode di sekitarnya.
- Mengubah banyak berkas yang tidak berkaitan, memformat ulang berkas utuh, mengganti pustaka yang sudah dipakai.
- Menulis ulang dari nol padahal cukup menambal.

**Keamanan dan ketahanan**
- Rahasia di dalam kode, SQL dengan string concat, `eval` atas input, `chmod 777`, menonaktifkan verifikasi TLS "agar jalan".
- Tidak ada timeout, retry, atau batas ukuran pada panggilan eksternal yang jelas membutuhkannya.

## Cara menghindarinya

1. **Baca dulu.** Lihat berkas sekitar, manifest dependensi, gaya tes, dan konvensi nama sebelum menulis. Tiru pola yang ada.
2. **Diff sekecil yang menyelesaikan masalah.** Jangan merapikan, mengganti nama, atau "sekalian" memperbaiki hal lain tanpa diminta; sebutkan temuan itu di catatan saja.
3. **Verifikasi hal yang tidak pasti**: tanda tangan fungsi, opsi CLI, versi pustaka. Cek dokumentasi, `--help`, atau kode sumber. Kalau tidak bisa dicek, katakan.
4. **Jalankan.** Eksekusi kode, tes, linter, build bila lingkungan memungkinkan. Laporkan hasil sebenarnya, termasuk yang gagal.
5. **Nama dari domain**: `overdueInvoices`, bukan `data`. Fungsi dinamai apa yang dilakukannya; variabel dinamai apa yang dikandungnya.
6. **Komentar menjelaskan mengapa**, bukan apa: keputusan non-obvious, batasan eksternal, rujukan ke tiket atau spesifikasi.
7. **Abstraksi setelah pengulangan nyata** (kira-kira tiga pemakaian), bukan sebelum.
8. **Galat ditangani di tempat yang bisa berbuat sesuatu**: gagal keras dengan pesan berguna, atau pulih dengan cara yang jelas dan tercatat. Jangan menelan.
9. **Tes menguji perilaku**, termasuk kasus tepi (kosong, null, batas, galat jaringan), bukan mengulang implementasi.
10. **Jujur tentang yang belum ada.** Jika sebagian sengaja ditinggalkan (stub, asumsi, belum dites), tandai di kode dan sebutkan di jawaban.

## Review kode (jika diminta mengaudit)

Urutkan temuan: risiko kerusakan data atau keamanan, lalu kebenaran logika, lalu ketahanan, lalu keterbacaan. Untuk tiap temuan: lokasi, masalah, dampak, perbaikan. Jangan membuka dengan pujian, dan jangan menyajikan selera pribadi sebagai temuan.

## Uji cepat

- Bisakah saya menunjuk dari mana setiap fungsi, flag, dan pustaka berasal, dan bahwa semuanya benar-benar ada?
- Kalau separuh diff ini dibuang, apakah masalah user tetap selesai? Jika ya, buang separuh itu.
- Apakah galat yang terjadi akan terlihat oleh seseorang?
