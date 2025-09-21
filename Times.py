def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    first_line = data[0].split()
    n = int(first_line[0])
    t = int(first_line[1])
    
    alunos = []
    for i in range(1, n + 1):
        line = data[i].split()
        nome = line[0]
        habilidade = int(line[1])
        alunos.append((nome, habilidade))
    
    alunos.sort(key=lambda x: x[1], reverse=True)
    
    times = [[] for _ in range(t)]
    
    for i in range(n):
        time_index = i % t
        times[time_index].append(alunos[i][0])
    
    for i in range(t):
        times[i].sort()
        print(f"Time {i + 1}")
        for nome in times[i]:
            print(nome)
        print() 

if __name__ == "__main__":
    main()