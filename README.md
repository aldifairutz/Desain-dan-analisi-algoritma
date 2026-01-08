0/1 Knapsack Problem: Optimasi Perlengkapan Touring MotorProyek ini adalah implementasi algoritma Dynamic Programming (DP) dan konsep Backtracking untuk menyelesaikan permasalahan 0/1 Knapsack. Kasus yang diangkat adalah optimasi pemilihan perlengkapan touring motor ke dalam tas/top box dengan kapasitas terbatas untuk mendapatkan keuntungan (profit) maksimal.📝 Deskripsi MasalahDalam kasus ini, seorang pengendara motor ingin membawa perlengkapan touring yang paling prioritas namun dibatasi oleh kapasitas penyimpanan sebesar 12 kg. Setiap barang hanya memiliki dua pilihan: diambil sepenuhnya ($1$) atau ditinggalkan ($0$) 1111
📦 Data Item (Kasus Riil)Berikut adalah daftar 10 item yang digunakan dalam optimasi ini:NoItemBerat (kg)Nilai (Profit)1Jaket Protector2.5852Tool Kit Set3.0953Jas Hujan1.5904Kompresor Ban1.0705Tenda 2P2.2806First Aid Kit0.5757Sepatu Boot1.8658Intercom Set0.8609Cooking Set1.25010Helm Cadangan1.640
🌳 State Space Tree & PruningPencarian solusi dilakukan dengan bantuan State Space Tree. Untuk meningkatkan efisiensi, diterapkan teknik Pruning (Pemangkasan) pada cabang yang melanggar kendala kapasitas ($w > 12$ kg).Simbol B: Menandakan branch yang dipangkas karena total berat melebihi ambang batas.Keunggulan: Mengurangi jumlah perhitungan dibandingkan metode Brute Force yang mengevaluasi seluruh $2^n$ kemungkinan kombinasi 4.🚀 Implementasi ProgramSolusi diimplementasikan menggunakan bahasa pemrograman Python dengan pendekatan Dynamic Programming untuk menjamin keoptimalan hasil.
📊 Hasil Analisis
Algoritma berhasil menemukan kombinasi item yang memberikan profit tertinggi dengan total berat yang tetap berada dalam batas 12 kg. Penggunaan teknik pruning terbukti mempercepat proses pencarian pada pohon ruang status dibandingkan metode evaluasi penuh.

Tugas Mata Kuliah Analisis Algoritma


Dosen Pengampu: Desi Anggreani, S.Kom., M.T., MOS.
