def main():
    level=int(input())
    for floor in range(0, level+1 ,1):
        for num in range (0,floor,1):
            print(num+1,end=" ")
        print("\n")
if __name__ =="__main__":
    main()
