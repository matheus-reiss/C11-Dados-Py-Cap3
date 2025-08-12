times = ["Real Madrid", "Barcelona", "Atletico Madrid", "Girona", "Real Betis"]

print("Top 3:", times[:3])

print("Últimos 2:", times[-2:])

print("Ordem alfabética:", sorted(times))

posicao_barcelona = times.index("Barcelona") + 1
print(f"Barcelona está na {posicao_barcelona} colocação.")