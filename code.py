from time import sleep 
#####TITLE#####
print("_"*20,"Ideal Gas Law Calculator","_"*20)
sleep(0.5)
print("CTRL+C to Exit Calculator")
sleep(0.5)


def enter(a):
    while True:
        try:
            x=float(input(a))
            if x>0:
                return x
                break
            else:
                print("Enter a valid value!")
                sleep(0.75)
                continue
        except ValueError:
            print("Enter a valid value!")
            sleep(0.75)
            continue

#####VARIABLES#####
constantR=0.08206
mole=volume=tempature=pressure=0

##MAIN FUNCTION##
while True:
    try:
        mole=enter("Enter Amount Of Substance(n):")
        sleep(0.25)
        volume=enter("Enter volume(L):")
        sleep(0.25)
        tempature=enter("Enter Tempature(K):")
        sleep(0.25)
        pressure=mole*constantR*tempature/volume
        print("Pressure={:.2f} atm".format(pressure))
        sleep(0.25)
        input("Press any key to continue\n")
    except KeyboardInterrupt:
        print("\nExiting...")
        sleep(1.25)
        exit()
