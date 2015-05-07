#secgen.py
#World Generation for Classic Traveller
#By Omer Golan-Joel
#Public Alpha v0.2

#import modules
import random
import string

#initialize global variables
sector_name="Default Sector"
realism=0
habitation=1
spacesize=1
row=1
column=1
min_row=1
min_column=1
max_row=8
max_column=10
subsector_row=1
minsubsector_row=1
maxsubsector_row=4
subsector_column=1
minsubsector_column=1
maxsubsector_column=4

#read config file
config=[]
inp = open("sec_cfg.txt","r")
for line in range(5):
    item=inp.readline().strip()
    config.append(item)
if config[0]=="real":
    realism=1
if config[0]=="canon":
    realism=0
if config[1]=="subsector":
    spacesize=1
if config[1]=="quadrant":
    spacesize=2
if config[1]=="sector":
    spacesize=3
if config[2]=="empty":
    habitation=0
if config[2]=="inhabited":
    habitation=1
sector_name=config[3]
file_name=config[4]

#set functions
def dice(n,sides): #Die-rolling function
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll

def starport_gen(): #Generates the starport digit
    starport=""
    throw=0
    throw=dice(2,6)
    if throw==2 or throw==3 or throw==4:
        starport="A"
    if throw==5 or throw==6:
        starport="B"
    if throw==7 or throw==8:
        starport="B"
    if throw==9:
        starport="D"
    if throw==10 or throw==11:
        starport="E"
    if throw==12:
        starport="X"
    return starport

def size_gen(): #Generates the size digit
    size=0
    size=dice(2,6)-2
    return size

def atmo_gen(): #Generates the atmosphere digit
    atmo=0
    atmo=dice(2,6)-7+UWP[1]
    if UWP[1]==0:
        atmo=0
    if atmo<0:
        atmo=0
    return atmo

def hyd_gen(): #Generates the hydrographics digit
    hyd=0
    hyd=dice(2,6)-7+UWP[2]
    if UWP[2]==0:
        hyd=hyd-4
    if UWP[2]==1:
        hyd=hyd-4
    if UWP[2]>=10:
        hyd=hyd-4
    if UWP[1]==0:
        hyd=0
    if hyd<0:
        hyd=0
    return hyd

def pop_gen(): #Generates the population digit
    pop=0
    pop=dice(2,6)-2
    return pop

def gov_gen(): #Generates the government digit
    gov=0
    gov=dice(2,6)-7+UWP[4]
    if gov<0:
        gov=0
    return gov

def law_gen(): #Generates the law-level digit
    law=0
    law=dice(2,6)-7+UWP[5]
    if law<0:
        law=0
    return law

def TL_gen(): #Generates the tech-level digit
    TL=0
    TL=dice(1,6)
    if UWP[0]=="A":
       TL=TL+6
    if UWP[0]=="B":
        TL=TL+4
    if UWP[0]=="C":
        TL=TL+2
    if UWP[0]=="X":
        TL=TL-4
    if UWP[1]==0 or UWP[1]==1:
        TL=TL+2
    if UWP[1]==2 or UWP[1]==3 or UWP[1]==4:
        TL=TL+1
    if UWP[2]<=3 or UWP[2]>=10:
        TL=TL+1
    if UWP[3]==9:
        TL=TL+1
    if UWP[3]>=10:
        TL=TL+2
    if UWP[4]<=5:
        TL=TL+1
    if UWP[5]==0 or UWP[5]==5:
        TL=TL+1
    if UWP[5]==13:
        TL=TL-2
    if UWP[4]==0:
        TL=0
    if TL<0:
        TL=0
    return TL

def base_gen(): #Generates the naval and scout bases
    scout=0
    naval=0
    base=" "
    throw1=0
    throw2=0
    throw1=dice(2,6)
    if UWP[0]=="A":
        throw1=throw1-3
    if UWP[0]=="B":
        throw1=throw1-2
    if UWP[0]=="C":
        throw1=throw1-1
    if throw1>=7:
        scout=1
    if UWP[0]=="E" or UWP[0]=="X":
                       scout=0
    throw2=dice(2,6)
    if throw2>=8:
        naval=1
    if UWP[0]=="C" or UWP[0]=="D" or UWP[0]=="E" or UWP[0]=="X":
                       naval=0
    if naval==0 and scout==0:
        base=" "
    if naval==0 and scout==1:
        base="S"
    if naval==1 and scout==1:
        base="2"
    if naval==1 and scout==0:
        base="N"
    return base

def pop_multi_gen(): #Generates the Population Multiplier
        pop_multi=0
        pop_multi=dice(1,9)
        return pop_multi

def belts_gen(): #Generates the Planetoid Belt number
        belts=0
        throw1=0
        throw2=0
        throw1=dice(2,6)
        if throw1>=8:
                throw2=dice(2,6)
                if throw2<=7:
                        belts=1
                if throw2>=8 and throw2<=11:
                        belts=2
                if throw2==12:
                        belts=3
        return belts

def GG_gen(): #Generates the Gas Giant number
        GG=0
        throw1=0
        throw2=0
        throw1=dice(2,6)
        if throw1<=10:
                throw2=dice(2,6)
                if throw2<=3:
                        GG=1
                if throw2>=4 and throw2<=5:
                        GG=2
                if throw2>=6 and throw2<=7:
                        GG=3
                if throw2>=8 and throw2<=10:
                        GG=4
                if throw2>=11:
                        GG=4
        return GG

def star_gen(): #generates stellar data
        n_stars=0
        size=""
        star_type=""
        startext1=""
        startext2=""
        startext3=""
        startext4=""
        startext=""
        throw=0
        throw1=0
        x=0
        tag=0
        decimal1=0
        decimal2=0
        decimal3=0
        primary=[]
        secondary=[]
        tretiary=[]
        throw=dice(2,6)
        if throw<=7:
                n_stars=1
        if throw>=8 and throw<=11:
                n_stars=2
        if throw==12:
                n_stars=3
        throw=dice(2,6) #generate primary star
        if UWP[2]>=4 and UWP[2]<=9:
                        throw=throw+4
                        tag=1
        if UWP[4]>=8 and tag==0:
                throw=throw+4
        if throw<=1:
                star_type="B"
        if throw==2:
                star_type="A"
        if throw>=3 and throw<=7:
                star_type="M"
        if throw==8:
                star_type="K"
        if throw==9:
                star_type="G"
        if throw>=10:
                star_type="F"
        decimal1=dice(1,10)-1
        throw1=dice(2,6)
        if UWP[2]>=4 and UWP[2]<=9:
                        throw1=throw1+4
                        tag=1
        if UWP[4]>=8 and tag==0:
                throw1=throw1+4
        if throw1<=0:
                size="Ia"
        if throw1==1:
                size="Ib"
        if throw1==2:
                size="II"
        if throw1==3:
                size="III"
        if throw1==4:
                size="IV"
        if throw1>=5 and throw1<=10:
                size="V"
        if throw1==11:
                size="VI"
        if throw1>=12:
                size="D"
        if size=="IV" and star_type=="K" and decimal1>=5:
                size="V"
        if size=="IV" and star_type=="M":
                size="V"
        if size=="VI" and star_type=="F" and decimal1<=4:
                size="V"
        if size=="VI" and star_type=="B":
                size="V"
        primary.append(star_type)
        if size!="D":
                primary.append(decimal1)
        primary.append(size)
        if size!="D":
                startext1="%s%s%s " % (primary[0], primary[1], primary[2])
        if size=="D":
                startext1="%s%s " % (primary[0], primary[1])
        if n_stars==2 or n_stars==3: #generate secondary star
                decimal2=0
                secondary=[]
                size=""
                star_type=""
                throw=dice(2,6)+throw1
                if throw==1:
                        star_type="B"
                if throw==2:
                        star_type="A"
                if throw==3 or throw==4:
                        star_type="F"
                if throw==5 or throw==6:
                        star_type="G"
                if throw==7 or throw==8:
                        star_type="K"
                if throw>=9:
                        star_type="M"
                decimal2=dice(1,10)-1
                throw=dice(2,6)+throw1
                if throw<=0:
                        size="Ia"
                if throw==1:
                        size="Ib"
                if throw==2:
                        size="II"
                if throw==3:
                        size="III"
                if throw==4:
                        size="IV"
                if throw==5 or throw==6:
                        size="D"
                if throw==7 or throw==8:
                        size="V"
                if throw==9:
                        size="VI"
                if throw>=10:
                        size="D"
                if size=="IV" and star_type=="K" and decimal2>=5:
                        size="V"
                if size=="IV" and star_type=="M":
                        size="V"
                if size=="VI" and star_type=="F" and decimal2<=4:
                        size="V"
                if size=="VI" and star_type=="B":
                        size="V"
                secondary.append(star_type)
                if size!="D":
                        secondary.append(decimal2)
                secondary.append(size)
                if size!="D":
                        startext2="%s%s%s " % (secondary[0], secondary[1], secondary[2])
                if size=="D":
                        startext2="%s%s " % (secondary[0], secondary[1])
        if n_stars==3: #generate tretiary star
                decimal3=0
                tretiary=[]
                size=""
                star_type=""
                throw=dice(2,6)+throw1
                if throw==1:
                        star_type="B"
                if throw==2:
                        star_type="A"
                if throw==3 or throw==4:
                        star_type="F"
                if throw==5 or throw==6:
                        star_type="G"
                if throw==7 or throw==8:
                        star_type="K"
                if throw>=9:
                        star_type="M"
                decimal3=dice(1,10)-1
                throw=dice(2,6)+throw1
                if throw<=0:
                        size="Ia"
                if throw==1:
                        size="Ib"
                if throw==2:
                        size="II"
                if throw==3:
                        size="III"
                if throw==4:
                        size="IV"
                if throw==5 or throw==6:
                        size="D"
                if throw==7 or throw==8:
                        size="V"
                if throw==9:
                        size="VI"
                if throw>=10:
                        size="D"
                if size=="IV" and star_type=="K" and decimal3>=5:
                        size="V"
                if size=="IV" and star_type=="M":
                        size="V"
                if size=="VI" and star_type=="F" and decimal3<=4:
                        size="V"
                if size=="VI" and star_type=="B":
                        size="V"
                tretiary.append(star_type)
                if size!="D":
                        tretiary.append(decimal3)
                tretiary.append(size)
                if size!="D":
                        startext3="%s%s%s " % (tretiary[0], tretiary[1], tretiary[2])
                if size=="D":
                        startext3="%s%s " % (tretiary[0], tretiary[1])
        startext4=startext1+startext2+startext3
        startext=string.join(startext4,'')
        return startext

def star_gen_r(): #generates realistic stellar data using Constantine Thomas' rules (version 3.0).
    n_stars=0
    size=""
    star_type=""
    startext1=""
    startext2=""
    startext3=""
    startext4=""
    startext=""
    throw=0
    throw1=0
    x=0
    tag=0
    decimal1=0
    decimal2=0
    decimal3=0
    primary=[]
    secondary=[]
    tretiary=[]
    throw=dice(2,6)
    if throw<=7:
        n_stars=1
    if throw>=8 and throw<=11:
        n_stars=2
    if throw==12:
        n_stars=3
    throw=dice(2,6) #generate primary star
    if UWP[2]>=4 and UWP[2]<=9:
        throw=throw+4
        tag=1
    if UWP[4]>=8 and tag==0:
        throw=throw+4
    if throw<=1:
        star_type="B"
    if throw==2:
        star_type="A"
    if throw>=3 and throw<=8:
        star_type="M"
    if throw==9:
        star_type="K"
    if throw==10:
        star_type="G"
    if throw>=11:
        star_type="F"
    if throw==12:
        star_type="K"
    if throw>=13:
        star_type="G"
    decimal1=dice(1,10)-1
    throw1=dice(2,6)
    if UWP[2]>=4 and UWP[2]<=9:
        throw1=throw1+4
        tag=1
    if UWP[4]>=8 and tag==0:
        throw1=throw1+4
    if throw1<=2:
        throw=dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
    if throw1==3:
        size="IV"
    if throw1>=4:
        size="V"
    if star_type=="A" or star_type=="F" or star_type=="G":
        if size=="D" or size=="II" or size=="III":
            size="V"
    if star_type=="M" and size=="IV":
        size="V"
    if star_type=="K" and size=="IV" and decimal1>=2:
        size="V"
    if size=="D" and UWP[2]>=1:
        size="V"
    if size=="D":
        star_type=""
        decimal1=""
    primary.append(star_type)
    primary.append(decimal1)
    primary.append(size)
    startext1="%s%s%s " % (primary[0], primary[1], primary[2])
    if n_stars==2 or n_stars==3: #generate secondary star
        decimal2=0
        secondary=[]
        size=""
        star_type=""
        throw=dice(2,6)
        if throw<=1:
            star_type="B"
        if throw<=2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal2=dice(1,10)-1
        throw1=dice(2,6)
        if throw1==2:
            throw=dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal2=""
        secondary.append(star_type)
        secondary.append(decimal2)
        secondary.append(size)
        startext2="%s%s%s " % (secondary[0], secondary[1], secondary[2])
    if n_stars==3: #generate tretiary star
        decimal3=0
        secondary=[]
        size=""
        star_type=""
        throw=dice(2,6)
        if throw<=1:
            star_type="B"
        if throw==2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal3=dice(1,10)-1
        throw1=dice(2,6)
        if throw1==2:
            throw=dice(1,6)
            if throw>=1 and throw<=3:
                size="D"
            if throw>=4 and throw<=5:
                size="III"
            if throw==6:
                size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal3=""
        tretiary.append(star_type)
        tretiary.append(decimal3)
        tretiary.append(size)
        startext3="%s%s%s " % (tretiary[0], tretiary[1], tretiary[2])

    startext4=startext1+startext2+startext3
    startext=string.join(startext4,'')
    return startext
    
#determine generated size
if spacesize==1:
        maxsubsector_row=1
        maxsubsector_column=1
        sector_name="Default Subsector"
if spacesize==2:
        maxsubsector_row=2
        maxsubsector_column=2
        sector_name="Default Quadrant"
if spacesize==3:
        maxsubsector_row=4
        maxsubsector_column=4
        sector_name="Default Sector"

#program body
outp = open(file_name,"w")
outp.write(sector_name+'\r\n')
outp.write(""+'\r\n')
outp.write("The data in the sector text files is laid out in column format:"+'\r\n')
outp.write(""+'\r\n')
outp.write(" 1-14: Name"+'\r\n')
outp.write("15-18: HexNbr"+'\r\n')
outp.write("20-28: UWP"+'\r\n')
outp.write("   31: Bases"+'\r\n')
outp.write("33-47: Codes & Comments"+'\r\n')
outp.write("   49: Zone"+'\r\n')
outp.write("52-54: PBG"+'\r\n')
outp.write("56-57: Allegiance"+'\r\n')
outp.write("59-74: Stellar Data"+'\r\n')
outp.write(""+'\r\n')
outp.write("....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8"+'\r\n')
outp.write(""+'\r\n')

for subsector_row in range (minsubsector_row, maxsubsector_row+1): #generate sector or quadrant
        for subsector_column in range (minsubsector_column, maxsubsector_column+1):
                for column in range (min_row, max_row+1): #generate subsector
                        for row in range (min_column, max_column+1):
                            throw=dice(1,6)
                            if throw>=4:
                                    if row<=9:
                                            row_loc="0%i" % (row)
                                    if row>=10:
                                            row_loc="%i" % (row)
                                    if column<=9:
                                            column_loc="0%i" % (column)
                                    if column>=10:
                                            column_loc="%i" % (column)
                                    location=column_loc+row_loc
                                    name="             "
                                    PBG=[0,0,0]
                                    UWP=[0,0,0,0,0,0,0,0]
                                    trade_codes=[]
                                    starport=starport_gen()
                                    UWP[0]=starport
                                    size=size_gen()
                                    UWP[1]=size
                                    atmo=atmo_gen()
                                    UWP[2]=atmo
                                    hyd=hyd_gen()
                                    UWP[3]=hyd
                                    pop=pop_gen()
                                    UWP[4]=pop
                                    gov=gov_gen()
                                    UWP[5]=gov
                                    law=law_gen()
                                    UWP[6]=law
                                    TL=TL_gen()
                                    UWP[7]=TL
                                    base=base_gen()
                                    pop_multi=pop_multi_gen()
                                    PBG[0]=pop_multi
                                    belts=belts_gen()
                                    PBG[1]=belts
                                    GG=GG_gen()
                                    PBG[2]=GG
                                    al="Na"
                                    if realism==0:
                                        stellar=star_gen()
                                    if realism==1:
                                        stellar=star_gen_r()

                                    #determine habitation
                                    if habitation==0:
                                        UWP[0]="X"
                                        UWP[4]=0
                                        UWP[5]=0
                                        UWP[6]=0
                                        UWP[7]=0
                                        PBG[0]=0
                                        base=""
                                        
                                    #Check for Trade Codes
                                    if UWP[2]>=4 and UWP[2]<=9 and UWP[3]>=4 and UWP[3]<=8 and UWP[4]>=5 and UWP[4]<=7:
                                            trade_codes.append("Ag")
                                    if UWP[1]==0 and UWP[2]==0 and UWP[3]==0:
                                            trade_codes.append("As")
                                    if UWP[4]==0:
                                            trade_codes.append("Ba")
                                    if UWP[2]>=2 and UWP[3]==0:
                                            trade_codes.append("De")
                                    if UWP[2]>=10 and UWP[3]>=1:
                                            trade_codes.append("Fl")
                                    if UWP[4]>=9:
                                            trade_codes.append("Hi")
                                    if UWP[2]<=1 and UWP[3]>=1:
                                            trade_codes.append("Ic")
                                    if UWP[2]<=2 or UWP[2]==4 or UWP[2]==7 or UWP[2]==9:
                                            if UWP[4]>=9:
                                                    trade_codes.append("In")
                                    if UWP[4]<=3 and realism==0:
                                            trade_codes.append("Lo")
                                    if UWP[4]<=3 and UWP[4]>=1 and realism==1:
                                            trade_codes.append("Lo")
                                    if UWP[2]<=3 and UWP[3]<=3 and UWP[4]>=6:
                                            trade_codes.append("Na")
                                    if UWP[4]<=6 and realism==0:
                                            trade_codes.append("Ni")
                                    if UWP[4]<=6 and UWP[4]>=1 and realism==1:
                                            trade_codes.append("Ni")
                                    if UWP[2]>=2 and UWP[2]<=5 and UWP[3]<=3:
                                            trade_codes.append("Po")
                                    if UWP[2]==6 or UWP[2]==8:
                                            if UWP[4]>=6 and UWP[4]<=8 and UWP[5]>=4 and UWP[5]<=9:
                                                    trade_codes.append("Ri")
                                    if UWP[2]==0:
                                            trade_codes.append("Va")
                                    if UWP[3]==10:
                                            trade_codes.append("Wa")
                                    trade_count=6-len(trade_codes)
                                    trade_count2=len(trade_codes)
                                    trade_space="   "*trade_count
                                    trade_list=string.join(trade_codes,' ')

                                    #Modify UWP for realism if desired
                                    if realism==1:
                                            if UWP[1]<=2 and UWP[2]>=10:
                                                    UWP[1]=3
                                            if UWP[1]<=2 and UWP[2]==1:
                                                    UWP[1]=3
                                            if UWP[1]<=3 and UWP[2]>=2 and UWP[2]<=5:
                                                    UWP[1]=4
                                            if UWP[1]<=4 and UWP[2]>=6 and UWP[2]<=9:
                                                    UWP[1]=5
                                            if UWP[4]==0:
                                                    PBG[0]=0
                                                    UWP[0]="X"
                                                    UWP[5]=0
                                                    UWP[6]=0
                                                    UWP[7]=0
                                                    base=" "
                                            if UWP[2]==4 and UWP[4]>=1 and UWP[7]<5:
                                                    UWP[7]=5
                                            if UWP[2]==7 and UWP[4]>=1 and UWP[7]<5:
                                                    UWP[7]=5
                                            if UWP[2]==9 and UWP[4]>=1 and UWP[7]<5:
                                                    UWP[7]=5
                                            if UWP[2]<=3 and UWP[4]>=1 and UWP[7]<7:
                                                    UWP[7]=7
                                            if UWP[2]==10 and UWP[4]>=1 and UWP[7]<8:
                                                    UWP[7]=8
                                            if UWP[2]==11 and UWP[4]>=1 and UWP[7]<8:
                                                    UWP[7]=8
                                            if UWP[2]==12 and UWP[4]>=1 and UWP[7]<9:
                                                    UWP[7]=9
                                            if UWP[2]==13 and UWP[4]>=1 and UWP[7]<7:
                                                    UWP[7]=7
                                            if UWP[0]=="A" and UWP[4]<=4:
                                                    UWP[4]=5
                                            if UWP[0]=="B" and UWP[4]<=2:
                                                    UWP[4]=3
                                            if UWP[0]=="A" and UWP[4]>=1 and UWP[7]<=8:
                                                    UWP[7]=9
                                            if UWP[0]=="B" and UWP[4]>=1 and UWP[7]<=6:
                                                    UWP[7]=7

                                    #Convert data to Traveller pseudo-hexadecimal
                                    if UWP[1]==10:
                                        UWP[1]="A"
                                    if UWP[2]==10:
                                        UWP[2]="A"
                                    if UWP[2]==11:
                                        UWP[2]="B"
                                    if UWP[2]==12:
                                        UWP[2]="C"
                                    if UWP[2]==13:
                                        UWP[2]="D"
                                    if UWP[2]==14:
                                        UWP[2]="E"
                                    if UWP[2]==15:
                                        UWP[2]="F"
                                    if UWP[3]>=10:
                                        UWP[3]="A"
                                    if UWP[4]==10:
                                        UWP[4]="A"
                                    if UWP[5]==10:
                                        UWP[5]="A"
                                    if UWP[5]==11:
                                        UWP[5]="B"
                                    if UWP[5]==12:
                                        UWP[5]="C"
                                    if UWP[5]==13:
                                        UWP[5]="D"
                                    if UWP[5]==14:
                                        UWP[5]="E"
                                    if UWP[5]==15:
                                        UWP[5]="F"
                                    if UWP[6]==10:
                                        UWP[6]="A"
                                    if UWP[6]==11:
                                        UWP[6]="B"
                                    if UWP[6]==12:
                                        UWP[6]="C"
                                    if UWP[6]==13:
                                        UWP[6]="D"
                                    if UWP[6]==14:
                                        UWP[6]="E"
                                    if UWP[6]==15:
                                        UWP[6]="F"
                                    if UWP[6]==16:
                                        UWP[6]="G"
                                    if UWP[6]==17:
                                        UWP[6]="H"
                                    if UWP[6]==18:
                                        UWP[6]="I"
                                    if UWP[6]==19:
                                        UWP[6]="J"
                                    if UWP[6]==20:
                                        UWP[6]="K"
                                    if UWP[7]==10:
                                        UWP[7]="A"
                                    if UWP[7]==11:
                                        UWP[7]="B"
                                    if UWP[7]==12:
                                        UWP[7]="C"
                                    if UWP[7]==13:
                                        UWP[7]="D"
                                    if UWP[7]==14:
                                        UWP[7]="E"
                                    if UWP[7]==15:
                                        UWP[7]="F"
                                    if UWP[7]==16:
                                        UWP[7]="G"
                                    if UWP[7]==17:
                                        UWP[7]="H"
                                    if UWP[7]==18:
                                        UWP[7]="I"
                                    if UWP[7]==19:
                                        UWP[7]="J"
                                    if UWP[7]==20:
                                        UWP[7]="K"

                                    #Eliminate starport if no population present
                                    if UWP[4]==0:
                                            UWP[0]="X"

                                    #Output result to file

                                ##    Old screen-display commands:
                                ##    if trade_count2!=0:
                                ##            print name, location, "%s%s%s%s%s%s%s-%s " % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), base, trade_list, trade_space, "%s%s%s" % (PBG[0], PBG[1], PBG[2]), al, stellar
                                ##    if trade_count2==0:
                                ##            print name, location, "%s%s%s%s%s%s%s-%s " % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), base, trade_space, "%s%s%s" % (PBG[0], PBG[1], PBG[2]), al, stellar
                                            
                                    if trade_count2!=0:
                                            line=name, location, "%s%s%s%s%s%s%s-%s " % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), base, trade_list, trade_space, "%s%s%s" % (PBG[0], PBG[1], PBG[2]), al, stellar
                                            line2=string.join(line,' ')
                                    if trade_count2==0:
                                            line=name, location, "%s%s%s%s%s%s%s-%s " % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), base, trade_space, "%s%s%s" % (PBG[0], PBG[1], PBG[2]), al, stellar
                                            line2=string.join(line,' ')
                                    outp.write(line2+'\r\n')
                min_row=min_row+8
                max_row=max_row+8
        min_row=1
        max_row=8
        min_column=min_column+10
        max_column=max_column+10
outp.close()

#write config file
if realism==0:
    reality="canon"
if realism==1:
    reality="real"
if spacesize==1:
    space="subsector"
if spacesize==2:
    space="quadrant"
if spacesize==3:
    space="sector"
if habitation==0:
    habitation2="empty"
if habitation==1:
    habitation2="inhabited"
outp = open("sec_cfg.txt","w")
outp.write(reality+'\r\n')
outp.write(space+'\r\n')
outp.write(habitation2+'\r\n')
outp.write(sector_name+'\r\n')
outp.write(file_name+'\r\n')
outp.close()
