


def split_data(x):
    lists=[]
    lists = x.split(':')
    return lists

def main():
    f = open('ipl_auction.txt','r')
    if f.mode == 'r':
        f1 = f.readlines()
        lists = []
        names=[]
        country=[]
        field = []
        cost=[]
        final_list = []
        india_list=[]
        overseas = []
        for x in f1:
            # print(x)
            # name,coutry,fild,costs = split_data(x)
            # names.append(name)
            # country.append(coutry)
            # field.append(fild)
            # cost.append(costs)
            lists = split_data(x)
            # print(lists)
            if lists[1] == "India":
                india_list.append(lists)
            else:
                overseas.append(lists)
            final_list.append(lists)
        #print(names,end="\n")
        #print((country).count("India"))
        print(overseas)

        #calculate
        batsmen = 0
        bowlers = 0
        all_rounders = 0
        wc = 0
        for i in india_list:
            if i[2] == "Batsman":
                batsmen += 1
            elif i[2] == "Bowler":
                bowlers += 1
            elif i[2] == "All-Rounder":
                all_rounders += 1
            else:
                wc += 1
        print(batsmen,bowlers,all_rounders,wc)
        batsmen = 0
        bowlers = 0
        all_rounders = 0
        wc = 0
        for i in overseas:
            if i[2] == "Batsman":
                batsmen += 1
            elif i[2] == "Bowler":
                bowlers += 1
            elif i[2] == "All-Rounder":
                all_rounders += 1
            else:
                wc += 1
        print(batsmen,bowlers,all_rounders,wc)






if __name__ == '__main__':
    main()
