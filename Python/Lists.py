if __name__ == '__main__':
    N = int(input())
    array = []

    for _ in range(N):
        raw_cmds = input().split()
        cmd = raw_cmds[0]
        args = raw_cmds[1:]
        if cmd == "print":
            print(array)
        else:
            cmd += "("+" ,".join(args)+")"
            eval("array."+cmd)
