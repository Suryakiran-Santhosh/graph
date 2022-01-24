
import graph.Disjoint_Set as disjoint_set

def main():
    ds = disjoint_set.Disjoint_Set(10)
    ds.union(1, 2)
    ds.union(2, 5)
    ds.union(5, 6)
    ds.union(6, 7)
    ds.union(3, 8)
    ds.union(8, 9)
    ds.show()

if __name__ == "__main__":
    main()