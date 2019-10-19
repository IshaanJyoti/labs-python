import sys

def main(argv):
    s = ""
    if len(argv) == 1:
        s = "Shivam Jyoti"
    else:
        for m in argv[1:]:
            s = s + " " + m
    print("Hello python to: "+s)

if __name__== "__main__":
  main(sys.argv)