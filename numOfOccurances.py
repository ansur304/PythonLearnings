class NumberOfOccurances:
    def __init__(self):
        pass

    def print_dup_removed(inList):
        out_list_dup = []
        for x in inList:
            if not out_list_dup.__contains__(x):
                out_list_dup.append(x)
        print(f" List after Removing duplicate :: {out_list_dup}")

    def read_input(self):
        try:
            in_list = []
            out_list = {}
            i = 0
            number = int(input("Enter the size of numbers ::"))
            print("Enter the numbers :: ")
            while i < number:
                in_list.append(input())
                i = i + 1
            print(f"input List :: %s " % in_list)
            for x in in_list:
                if not out_list.keys().__contains__(x):
                    out_list[x] = 1
                else:
                    occur = out_list.get(x) + 1
                    out_list.pop(x)
                    out_list[x] = occur
            for i in out_list:
                print(f" key : {i} value ::{out_list.get(i)} ")
            self.print_dup_removed(in_list)

        except ValueError:
            print("Invalid value !")
        except ZeroDivisionError:
            print("Zero can not be devided !")
