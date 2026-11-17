---
name: anti-slop
description: Cegah output AI yang generik, template, dan "terasa buatan AI" (slop) di semua bidang - desain UI/web, kode, tulisan/copywriting, motion graphic/video/presentasi, serta riset dan klaim faktual. Pakai skill ini setiap kali user meminta Claude membuat atau memperbaiki sesuatu (website, aplikasi, komponen, kode, artikel, caption, naskah, dubbing, slide, storyboard, laporan), atau menyebut "anti slop", "jangan generik", "jangan kelihatan buatan AI", "lebih natural", "lebih manusiawi", "bagus dan unik", "profesional", "review/audit hasil ini". Gunakan juga sebagai pemeriksaan akhir sebelum menyerahkan hasil kerja apa pun, walau user tidak menyebut kata slop. Use whenever output could come out generic, templated, padded, or AI-sounding (design, code, writing, media, research).
---

# Anti-Slop

Slop adalah output yang secara teknis benar tetapi tidak dibuat untuk siapa pun secara khusus. Ia lahir saat model memilih jawaban yang paling mungkin muncul (font default, struktur artikel baku, abstraksi berlebih, kalimat pembuka klise) alih-alih keputusan yang dibuat untuk konteks ini. Pembaca mengenalinya dalam hitungan detik, dan sesudah itu mereka berhenti percaya pada sisanya.

Obatnya bukan "tambah gaya". Obatnya: **buat keputusan spesifik, buang pengisi, lalu verifikasi.**

## Alur kerja

1. **Tangkap konteks.** Siapa audiensnya, untuk apa, di mana dipakai, apa batasannya (stack, brand, durasi, bahasa, nada). Kalau jawabannya sudah ada di percakapan atau file, pakai. Tanya hanya jika satu hal yang belum diketahui akan mengubah hasil secara besar, dan maksimal satu pertanyaan.
2. **Putuskan arah sebelum mengerjakan.** Tulis di kepala (atau satu-dua baris di awal jawaban untuk tugas besar): arah visual/nada/arsitektur yang dipilih, dan alasannya. Arah yang bisa dijelaskan alasannya biasanya bukan slop.
3. **Kerjakan** dengan detail nyata: konten sungguhan, nama domain, angka yang bisa dipertanggungjawabkan.
4. **Audit slop.** Buka referensi domain yang relevan (tabel di bawah) dan periksa hasilnya terhadap daftar tandanya. Untuk file teks/kode/CSS, jalankan `scripts/slop_scan.py <file>` sebagai pemindai awal. Skrip hanya menangkap pola permukaan, jadi tetap nilai sendiri.
5. **Revisi, lalu laporkan jujur.** Perbaiki temuan. Jangan klaim sesuatu sudah dites, dicek, atau selesai kalau belum benar-benar dijalankan.

## Prinsip lintas bidang

- **Spesifik mengalahkan aman.** Kalau suatu elemen bisa dipindah ke proyek lain tanpa diubah, ia generik. Ganti dengan sesuatu yang hanya cocok di sini.
- **Setiap elemen harus punya alasan.** Gradien, komentar, bagian artikel, abstraksi, animasi, bullet: tanya "kalau dihapus, apa yang hilang?" Kalau tidak ada, hapus.
- **Konten nyata, bukan penanda.** Lorem ipsum, "John Doe", statistik karangan, testimoni palsu, `// TODO: implement`, dan "10.000+ pengguna" yang tidak ada sumbernya adalah slop, apalagi bila disajikan seolah asli.
- **Panjang mengikuti kebutuhan.** Pertanyaan singkat dijawab singkat. Jangan menambah ringkasan, penutup, atau "semoga membantu".
- **Ikuti yang sudah ada.** Di proyek yang sudah berjalan, gaya kode, desain, dan istilah yang ada lebih penting daripada selera sendiri.
- **Jangan mengarang.** API, library, kutipan, sumber, angka, dan fitur produk harus diverifikasi atau diberi label tidak yakin. Fakta yang bisa berubah dicari dulu.
- **Anti-slop bukan anti-konvensi.** Pola standar yang berguna (navigasi di atas, tombol berwarna jelas, `try/catch` di batas I/O, struktur tulisan yang mudah dipindai) tetap dipakai. Yang dihindari adalah default yang dipilih tanpa berpikir.

## Peta referensi

Baca hanya yang relevan dengan tugas. Tugas campuran (misalnya landing page lengkap dengan copy) membaca lebih dari satu.

| Tugas | Baca |
|---|---|
| Website, UI, komponen, dashboard, poster, logo, layout | `references/design.md` |
| Menulis atau mengubah kode, skrip, query, konfigurasi, review kode | `references/code.md` |
| Artikel, caption, email, copy, naskah, terjemahan, balasan chat | `references/writing.md` |
| Motion graphic, video, storyboard, voice-over, slide, gambar AI | `references/media.md` |
| Riset, analisis, angka, rujukan, laporan, klaim "sudah selesai/sudah dites" | `references/facts-and-claims.md` |

Jika pengguna juga punya skill khusus (misalnya `frontend-design`), skill itu mengatur cara membangun; skill ini menjadi pemeriksa mutu di atasnya, bukan penggantinya.

## Format hasil

- Untuk tugas pembuatan: serahkan hasilnya, plus paling banyak 2-3 kalimat tentang keputusan utama dan asumsi. Jangan melampirkan daftar "yang sudah saya lakukan agar tidak slop".
- Untuk permintaan audit atau review: gunakan format ini.
  1. Vonis satu kalimat.
  2. Temuan, diurutkan dari yang paling merusak, masing-masing dengan lokasi, mengapa itu slop, dan perbaikan konkret.
  3. Versi yang sudah diperbaiki, jika diminta atau kecil saja.
- Jika ada hal yang tidak bisa diverifikasi (tidak bisa menjalankan kode, tidak ada akses internet), sebutkan secara singkat di bagian akhir.
