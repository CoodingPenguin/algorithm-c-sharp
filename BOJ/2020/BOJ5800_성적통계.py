for _ in range(int(input())):
    ns = sorted(list(map(int, input().split()))[1:], reverse=True)
    diff = [ns[i] - ns[i+1] for i in range(len(ns)-1)]

    print(f"Class {_+1}")
    print(f"Max {max(ns)}, Min {min(ns)}, Largest gap {max(diff)}")
