from Driver import Wave

def main():
    while True:
        print("""*-------------------------------------------------------------------------------------------------------------------*
|0. exit                 | quit program                                                                             |
|1. heightmap autocreate | create a new heightmap with provided settings and apply smoothening+colouring            |
|2. smooth heightmap     | reduce errors in heightmap by averaging pixel values [open any created heightmap] +colour|
|3. colour heightmap     | colour the heightmap based on ranges in coloursettings.py [colour any created heightmap] |
*-------------------------------------------------------------------------------------------------------------------*""")

        try:
            option = int(input("operation > ").strip())

        except ValueError:
            print("enter number from given list")
            continue

        if option == 0:
            print("bye bye")
            break
        
        elif option == 1:
            try:
                height = int(input("height* > ").strip())
                width = int(input("width* > ").strip())
                cap = int(input("effect radius* = ").strip())
                zmooth = int(input("smoothness value (default 5)> ").strip())
                savee = input("save name/path (leave for default) > ").strip()
            
            except ValueError:
                print("one or more values are not integer")
                continue
                
            if (savee == "" or savee is None) and (zmooth == "" or zmooth is None):
                Wave(height=height, width=width, cap=cap).create()
            elif savee == "" or savee is None:
                Wave(height=height, width=width, cap=cap, smoothval=zmooth).create()
            elif zmooth == "" or zmooth is None:
                Wave(height=height, width=width, cap=cap, savename=savee).create()
            else:
                Wave(height=height, width=width, cap=cap, savename=savee, smoothval=zmooth).create()

        elif option == 2:
            location = input("path to heightmap > ").strip()
            try:
                smoothness = int(input("smoothness values > ").strip())
                Wave(None, None, None, smoothval=smoothness).heightmap_smoothner(openfile=location)

            except ValueError:
                print("smoothness value must be a number.")

        elif option == 3:
            location = input("path to heightmap > ").strip()
            Wave(None, None, None, None, None).heightmap_colour(matrix=None, openfile=location)


        else:
            print("invalid operation")

if __name__ == "__main__":
    print("~~ heightmap generator ~~")

    main()

# gen = Wave(height=16384,
#             width=16384,
#             cap=2500,
#             savename="trippingedit")

# smoo = gen.heightmap_smoothner(smoothval=50, openfile="tripping.png")
# gen.heightmap_colour(smoo)
