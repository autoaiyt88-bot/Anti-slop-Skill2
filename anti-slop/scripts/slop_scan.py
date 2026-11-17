#!/usr/bin/env python3
"""Pemindai pola slop permukaan.

Pemakaian:
    python slop_scan.py <berkas> [<berkas> ...]
    python slop_scan.py --text "teks langsung"

Skrip ini hanya menangkap pola yang mudah dikenali dengan regex. Ia tidak
menilai kualitas. Lolos pemindaian bukan berarti bebas slop, dan temuan
bukan otomatis salah: nilai konteksnya sebelum mengubah apa pun.
"""
import re
import sys
from pathlib import Path

# (kategori, pola regex, penjelasan singkat)
RULES = [
    # Tulisan, Indonesia
    ("tulisan", r"di era (digital|modern|globalisasi)[^.\n]{0,40}", "pembuka latar luas"),
    ("tulisan", r"dalam dunia yang (terus )?(berkembang|berubah)", "pembuka latar luas"),
    ("tulisan", r"tidak dapat dipungkiri", "frasa pengisi"),
    ("tulisan", r"perlu (dicatat|diingat|dipahami) bahwa", "frasa pengisi"),
    ("tulisan", r"sangat penting untuk", "frasa pengisi"),
    ("tulisan", r"mari kita (selami|jelajahi|kupas|bahas)", "ajakan klise"),
    ("tulisan", r"sebagai kesimpulan", "penutup pengulang"),
    ("tulisan", r"semoga (artikel|jawaban|penjelasan) ini (bermanfaat|membantu)", "penutup klise"),
    ("tulisan", r"jangan ragu untuk", "penutup klise"),
    ("tulisan", r"solusi (inovatif|terbaik|all-in-one)|revolusioner|transformatif", "klise pemasaran"),
    ("tulisan", r"pertanyaan (yang )?(bagus|menarik)", "pujian pembuka"),
    # Tulisan, Inggris
    ("tulisan", r"\bdelve(s|d)?\b|\btapestry\b|\brealm of\b|\ba testament to\b", "kata khas AI"),
    ("tulisan", r"in today's (fast-paced|digital|ever-changing)", "pembuka latar luas"),
    ("tulisan", r"it'?s (worth noting|important to note)", "frasa pengisi"),
    ("tulisan", r"it'?s not (just|only) [^.\n]{1,60}, it'?s", "pola 'bukan sekadar X, tapi Y'"),
    ("tulisan", r"\b(game-changer|seamless(ly)?|unlock the (power|potential)|leverage)\b", "klise pemasaran"),
    ("tulisan", r"great question|i hope this helps|in conclusion,", "pembuka/penutup klise"),
    # Desain
    ("desain", r"lorem ipsum", "teks penanda"),
    ("desain", r"\b(john|jane) doe\b|feature (one|two|three)\b", "konten penanda"),
    ("desain", r"font-family:[^;]*\b(inter|roboto|arial)\b", "font default; pastikan memang dipilih"),
    ("desain", r"linear-gradient\([^)]*(#?(6366f1|8b5cf6|a855f7|7c3aed|667eea|764ba2))", "gradien ungu-biru khas"),
    ("desain", r"from-(purple|violet|indigo)-\d+[^\"'\n]{0,40}to-(pink|blue|indigo|purple)-\d+", "gradien Tailwind khas"),
    ("desain", r"backdrop-blur|backdrop-filter:\s*blur", "glassmorphism; pastikan berfungsi"),
    ("desain", r"\b\d{1,3}(,\d{3})*\+?\s*(happy )?(customers|users|pengguna|pelanggan)\b", "statistik mungkin karangan"),
    # Kode
    ("kode", r"(//|#)\s*TODO:?\s*implement", "implementasi pura-pura"),
    ("kode", r"console\.log\(", "log debugging tertinggal?"),
    ("kode", r"catch\s*(\([^)]*\))?\s*\{\s*\}", "galat ditelan"),
    ("kode", r"except[^\n:]*:\s*\n\s*pass\b", "galat ditelan"),
    ("kode", r"(//|#)\s*(increment|decrement|return|loop|initialize|define)\b", "komentar yang mengulang kode"),
    ("kode", r"\b(handleStuff|processData|doSomething|tempData|myFunction)\b", "nama generik"),
    ("kode", r"(password|secret|api[_-]?key|token)\s*[:=]\s*['\"][^'\"]{6,}['\"]", "rahasia di dalam kode?"),
]

COMPILED = [(c, re.compile(p, re.IGNORECASE), why) for c, p, why in RULES]
EM_DASH = "\u2014"


def scan(label, text):
    findings = []
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        for cat, rx, why in COMPILED:
            m = rx.search(line)
            if m:
                findings.append((lineno, cat, why, m.group(0).strip()))
    # Pola yang dihitung per dokumen
    words = max(1, len(text.split()))
    dashes = text.count(EM_DASH)
    if dashes and dashes / words > 1 / 120:
        findings.append((0, "tulisan", "tanda pisah panjang terlalu sering", f"{dashes} kali dalam {words} kata"))
    bullets = sum(1 for l in lines if re.match(r"\s*([-*\u2022]|\d+[.)])\s", l))
    if len(lines) > 8 and bullets / len(lines) > 0.6:
        findings.append((0, "tulisan", "hampir semua baris berupa butir", f"{bullets}/{len(lines)} baris"))
    return findings


def report(label, text):
    findings = scan(label, text)
    print(f"== {label}: {len(findings)} temuan")
    for lineno, cat, why, snippet in findings:
        where = f"baris {lineno}" if lineno else "dokumen"
        print(f"  [{cat}] {where}: {why} -> {snippet[:80]}")
    return len(findings)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    total = 0
    if argv[1] == "--text":
        total += report("teks", " ".join(argv[2:]))
    else:
        for name in argv[1:]:
            path = Path(name)
            if not path.is_file():
                print(f"== {name}: tidak ditemukan")
                continue
            total += report(name, path.read_text(encoding="utf-8", errors="replace"))
    print(f"\nTotal temuan: {total}. Ini petunjuk, bukan vonis; nilai konteksnya.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
