def main():
    inlist = input().split()
    inlist2 = input().split()
    inlist_all = inlist + inlist2
    inlist_all.sort()
    print(" ".join(inlist_all))


if __name__ == "__main__":
    main()

