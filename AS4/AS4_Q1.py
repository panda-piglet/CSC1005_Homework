def HanoiTower(level,start = "A", tmp = "B", end = "C"):
    if level == 1:
        print(f"{start} -> {end}")
    else:
        #先把上面的圆盘全部移到中间
        HanoiTower(level - 1,start, end , tmp)
        #移动最底下的一个大圆盘
        print(f"{start} -> {end}")
        #最后把中间的圆盘移到右边
        HanoiTower(level -1 ,tmp , start ,end)
def main():
    HanoiTower(3)
if __name__ == "__main__":
    main()
