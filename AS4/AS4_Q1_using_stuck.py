def HanoiTower(level):
    stuck = [(level,"A","B","C")]
    while len(stuck) != 0:
        state = stuck.pop(-1)
        if state [0] == 1:
            print(f"{state[1]} -> {state[3]}")
        else:
            stuck.append((state[0] - 1,state[2],state[1],state[3]))
            stuck.append((1,state[1],state[2],state[3]))
            stuck.append((state[0] - 1,state[1],state[3],state[2]))
            
def main():
    HanoiTower(3)
if __name__ =="__main__":
    main()
