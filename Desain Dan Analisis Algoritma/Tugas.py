def solve_touring_knapsack():
    # Data: (Nama, Berat dalam kg, Profit/Prioritas)
    items = [
        ("Jaket Protector", 2.5, 85), ("Tool Kit Set", 3.0, 95),
        ("Jas Hujan", 1.5, 90), ("Kompresor Ban", 1.0, 70),
        ("Tenda 2P", 2.2, 80), ("First Aid Kit", 0.5, 75),
        ("Sepatu Boot", 1.8, 65), ("Intercom Set", 0.8, 60),
        ("Cooking Set", 1.2, 50), ("Helm Cadangan", 1.6, 40)
    ]
    
    M = 12.0  # Kapasitas 12 kg
    # Konversi ke integer (kali 10) untuk indeks tabel DP
    M_int = int(M * 10)
    n = len(items)
    
    dp = [[0 for _ in range(M_int + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, w, p = items[i-1]
        w_int = int(w * 10)
        for j in range(M_int + 1):
            if w_int <= j:
                dp[i][j] = max(p + dp[i-1][j-w_int], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
                
    # Melacak item yang dipilih
    selected = []
    curr_w = M_int
    for i in range(n, 0, -1):
        if dp[i][curr_w] != dp[i-1][curr_w]:
            selected.append(items[i-1])
            curr_w -= int(items[i-1][1] * 10)
            
    return dp[n][M_int], selected, (M_int - curr_w) / 10

profit, items_picked, weight = solve_touring_knapsack()
print(f"Total Nilai Prioritas: {profit}")
print(f"Total Berat Terpakai: {weight} kg")
print("Daftar Perlengkapan Terpilih:")
for item in items_picked:
    print(f"- {item[0]} ({item[1]} kg, Nilai: {item[2]})")