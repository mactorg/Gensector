#gensec.py
#World Generation for Classic Traveller
#By Omer Golan-Joel
#Updated by MacTORG
#Cleaned up output and added Cx and Ix and adjusted UWP and PBG.
#Public Alpha v0.3

import random
import string
import time

#initialize global variables
sector_name="Default Sector"
sector_type="subsector"
density="standard"
realism=0
habitation=1
spacesize=1
row=1
column=1
min_row=1
min_column=1
max_row=10
max_column=8
subsector_row=1
subsector_column=1
totsystems=0
name="               "
PBG=[0,0,0]
UWP=[0,0,0,0,0,0,0,0]
sector_density=[1,6,3]  # Standard density 
trade_codes=[]

#read config file
config=[]
inp = open("gensec.conf","r")
for line in range(6):
    item=inp.readline().strip()
    config.append(item)
if config[0]=="real":
    realism=1
if config[0]=="canon":
    realism=0
if config[1]=="subsector":
    spacesize=1
if config[1]=="sector":
    spacesize=2
if config[2]=="empty":
    habitation=0
if config[2]=="inhabited":
    habitation=1
sector_name=config[3]
file_name=config[4]
density=config[5]
if config[5]=="galactic":
	sector_density=[3,6,3]
if config[5]=="rift":
	sector_density=[2,6,2]
if config[5]=="sparse":
	sector_density=[1,6,1]
if config[5]=="scattered":
	sector_density=[1,6,2]
if config[5]=="standard":
	sector_density=[1,6,3]
if config[5]=="dense":
	sector_density=[1,6,4]
if config[5]=="cluster":
	sector_density=[1,6,5]
if config[5]=="core":
	sector_density=[2,6,11]
	

#set functions
def dice(n,sides): #Die-rolling function
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll
def toHex(dec):
	x = (dec % 21)
	digits = "0123456789ABCDEFGHIJK"
	rest = dec / 21
	if (rest == 0):
		return digits[x]
		return toHex(rest) + digits[x]

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

def gensys():
	name="               "
	PBG=[0,0,0]
	UWP=[0,0,0,0,0,0,0,0]
	trade_codes=[]
# Generates the starport digit
	starport=""
	throw=0
	throw=dice(2,6)
	if throw==2 or throw==3 or throw==4:
		starport="A"
	if throw==5 or throw==6:
		starport="B"
	if throw==7 or throw==8:
		starport="C"
	if throw==9:
		starport="D"
	if throw==10 or throw==11:
		starport="E"
	if throw==12:
		starport="X"
	UWP[0]=starport
# Generates the size digit
	size=0
	size=dice(2,6)-2
	if size==0:
		size=0
	if size==10:
		size=dice(1,6)+9
	UWP[1]=size
# Generates the atmosphere digit
	atmo=dice(2,6)-7+size
	if size==0:
		atmo=0
	if atmo<0:
		atmo=0
	if atmo>15:
		atmo=15
	UWP[2]=atmo
# Generates the hydrographics digit
	hyd=dice(2,6)-7+atmo
	if atmo==0:
		hyd=hyd-4
	if atmo==1:
		hyd=hyd-4
	if atmo>=10:
		hyd=hyd-4
	if size==0:
		hyd=0
	if hyd<0:
		hyd=0
	UWP[3]=hyd
# Generates the population digit
	pop=0
	pop=dice(2,6)-2
	if pop==10:
		pop=dice(1,6)+9
	UWP[4]=pop
# Generates the government digit
	gov=0
	gov=dice(2,6)-7+pop
	if gov<0:
		gov=0
	if gov>15:
		gov=15
	UWP[5]=gov
# Generates the law-level digit
	law=0
	law=dice(2,6)-7+gov
	if law<0:
		law=0
	if law>20:
		law=20
	UWP[6]=law
# Generates the tech-level digit
	TL=0
	TL=dice(1,6)
	if starport=="A":
		TL=TL+6
	if starport=="B":
		TL=TL+4
	if starport=="C":
		TL=TL+2
	if starport=="X":
		TL=TL-4
	if starport=="F":
		TL=TL+1
	if size==0 or size==1:
		TL=TL+2
	if size==2 or size==3 or size==4:
		TL=TL+1
	if atmo<=3 or atmo>=10:
		TL=TL+1
	if hyd==9:
		TL=TL+1
	if hyd>=10:
		TL=TL+2
	if pop<=5:
		TL=TL+1
	if pop==9:
		TL=TL+2
	if pop==10:
		TL=TL+4
	if gov==0 or gov==5:
		TL=TL+1
	if gov==13:
		TL=TL-2
	if pop==0:
		TL=0
	if TL<0:
		TL=0
	UWP[7]=TL
# Generates the naval and scout bases
	scout=0
	naval=0
	base="  "
	throw1=0
	throw2=0
	throw1=dice(2,6)
	throw2=dice(2,6)
	if throw1<=6 and starport=="A":
		naval=1
		if throw2<=4:
			scout=1
	if throw1<=5 and starport=="B":
		naval=1
		if throw2<=5:
			scout=1
	if throw2<=6 and starport=="C":
		scout=1
	if throw2<=7 and starport=="D":
		scout=1
	if naval==0 and scout==0:
		base="  "
	if naval==0 and scout==1:
		base=" S"
	if naval==1 and scout==1:
		base="NS"
	if naval==1 and scout==0:
		base="N "
# Generates the Population Multiplier
	pop_multi=0
	while pop_multi==0:
		pop_multi=dice(2,6)-2
	if pop_multi>9:
		pop_multi=9
	if pop==0:
		pop_multi=0
	PBG[0]=pop_multi
# Generates the Planetoid Belt number
	belts=0
	belts=dice(1,6)-3
	if belts<0:
		belts=0
	PBG[1]=belts
# Generates the Gas Giant number
	GG=0
	GG=dice(2,6)/2-2
	if GG<0:
		GG=0
	PBG[2]=GG
# Generates Worlds counter
	worlds=0
	worlds=dice(2,6)+GG+belts+1
    
	al="Im"
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
		base="  "
                                        
	#Check for Trade Codes
	if UWP[2]>=4 and UWP[2]<=9 and UWP[3]>=4 and UWP[3]<=8 and UWP[4]>=5 and UWP[4]<=7:
		trade_codes.append("Ag")
	if UWP[1]==0 and UWP[2]==0 and UWP[3]==0:
		trade_codes.append("As")
	if UWP[4]==0:
		trade_codes.append("Ba")
	if UWP[2]>=2 and UWP[3]==0:
		trade_codes.append("De")
	if UWP[2]>=10 and UWP[2]<=12 and UWP[3]>=1:
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
	if UWP[4]>=4 and UWP[4]<=6 and realism==0:
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
	if UWP[1]>=5 and UWP[1]<=9 and UWP[3]==10:
		trade_codes.append("Wa")
	if pop>=5:
		trade_codes.append("Pz")
	if pop>=0 and pop<=6:
		trade_codes.append("Da")
		
	trade_count=6-len(trade_codes)
	trade_count2=len(trade_codes)
	trade_space="   "*trade_count
	trade_space2="  "
	trade_list=string.join(trade_codes,' ')
# Generate Z code
	tzone=" G"
	if pop<=6:
		tzone="Da"
	if pop>=7:
		tzone="Pu"
# Generates the Ix
	Ix=0
	Ixsign=""
	if starport=="A" or starport=="B":
		Ix=Ix+1
	if starport=="D" or starport=="E" or starport=="X":
		Ix=Ix-1
	if TL>=10:
		Ix=Ix+1
	if TL<=8:
		Ix=Ix-1
	if "Ag" in trade_codes:
		Ix=Ix+1
	if "Hi" in trade_codes:
		Ix=Ix+1
	if "In" in trade_codes:
		Ix=Ix+1
	if "Ri" in trade_codes:
		Ix=Ix+1
	if pop<=6:
		Ix=Ix-1
	if base=="NS":
		Ix=Ix+1
	if Ix>=0:
		Ixsign="+"
# Generate the Ex
	Ex=""
	Exr=0
	Exl=0
	Exi=0
	Exe=0
	Exesign=""
	Exr=dice(2,6)
	if TL>=8:
		Exr=Exr+GG+belts
	Exl=pop-1
	if Exl<0:
		Exl=0
	Exi=dice(2,6)+Ix
	if "Ba" in trade_codes or "Di" in trade_codes or "Lo" in trade_codes:
		Exi=0
	if "Ni" in trade_codes:
		Exi=dice(1,6)
	if Exi<0:
		Exi=0
	Exe=dice(1,6)-3
	if Exe>=0:
		Exesign="+"
	Exr=toHex(Exr)
	Exl=toHex(Exl)
	Exi=toHex(Exi)
	Ex="(%s%s%s%s%s)" % (Exr,Exl,Exi,Exesign,Exe)
# Generate the Cx
	Cx=""
	Cxh=0
	Cxa=0
	Cxst=0
	Cxsy=0
	Cxh=dice(1,6)-3+pop
	if Cxh<1:
		Cxh=1
	Cxa=pop+Ix
	if Cxa<1:
		Cxa=1
	Cxst=dice(1,6)-3+5
	if Cxst<1:
		Cxst=1
	Cxsy=dice(1,6)-3+TL
	if Cxsy<1:
		Cxsy=1
	Cxh=toHex(Cxh)
	Cxa=toHex(Cxa)
	Cxsy=toHex(Cxsy)
	Cx="[%s%s%s%s]" % (Cxh,Cxa,Cxst,Cxsy)

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
			base="  "
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
	UWP[1]=toHex(UWP[1])
	UWP[2]=toHex(UWP[2])
	UWP[3]=toHex(UWP[3])
	UWP[4]=toHex(UWP[4])
	UWP[5]=toHex(UWP[5])
	UWP[6]=toHex(UWP[6])
	UWP[7]=toHex(UWP[7])
	#Eliminate starport if no population present
	if UWP[4]==0:
		UWP[0]="X"

	# screen-display commands:
	if trade_count2!=0:
		print location, name, "%s%s%s%s%s%s%s-%s" % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), trade_list, trade_space, trade_space2, " {%s%s}" % (Ixsign,Ix),Ex,Cx,"-", base, tzone, " %s%s%s" % (PBG[0], PBG[1], PBG[2]), "%02d" % worlds, al, "   ", stellar
	if trade_count2==0:
		print location, name, "%s%s%s%s%s%s%s-%s" % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), trade_space, trade_space2, " {%s%s}" % (Ixsign,Ix),Ex,Cx,"-", base, tzone, " %s%s%s" % (PBG[0], PBG[1], PBG[2]), "%02d" % worlds, al, "   ", stellar

	#Output result to file
	if trade_count2!=0:
		line=location, name, "%s%s%s%s%s%s%s-%s" % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), trade_list, trade_space, trade_space2, " {%s%s}" % (Ixsign,Ix),Ex,Cx,"-", base, tzone, " %s%s%s" % (PBG[0], PBG[1], PBG[2]), "%02d" % worlds, al, "   ", stellar
		line2=string.join(line,' ')
	if trade_count2==0:
		line=location, name, "%s%s%s%s%s%s%s-%s" % (UWP[0],UWP[1],UWP[2],UWP[3],UWP[4],UWP[5],UWP[6],UWP[7]), trade_space, trade_space2, " {%s%s}" % (Ixsign,Ix),Ex,Cx,"-", base, tzone, " %s%s%s" % (PBG[0], PBG[1], PBG[2]), "%02d" % worlds, al, "   ", stellar
		line2=string.join(line,' ')
	outp.write(line2+'\r\n')
    
#determine generated size

if spacesize==1:
	column = 1
	min_column = column
	max_column = column + 8
	row = 1
	min_row = row
	max_row = row + 10
	sector_type="Subsector"
if spacesize==2:
	column=1
	row=1
	min_column=column
	min_row=row
	max_column=33
	max_row=41
	sector_type="Sector"

#Main - Start of program

outp = open(file_name,"w")
outp.write("<sec>"+'\r\n')
outp.write("<meta "+sector_type+"UID=\"mw-orion-5812\""+'\r\n')
outp.write("      tlCap=\"21\""+'\r\n')
outp.write("      density=\""+density+"\""+'\r\n')
outp.write("      civil=\"Civilized\""+'\r\n')
outp.write("      generated=\""+time.strftime("%c")+"\""+'\r\n')
outp.write("      systems="+'\r\n')
outp.write("      hash=\"SHA256\""+'\r\n')
outp.write("      prng=\"burtle\""+'\r\n')
outp.write("      />"+'\r\n')
outp.write("<data>"+'\r\n')
outp.write("Hex  Name            UWP       Remarks                {Ix} (Ex)    [Cx]   N B  Z   PBG W  A      Stellar       "+'\r\n')
outp.write("---- --------------- --------- ---------------------- ---- ------- ------ - -- --  --- -- ------ --------------"+'\r\n')
print "<sec>\r"
print "<meta %sUID=\"mw-orion-5812\"" % sector_type
print "Type: %s" % sector_type
print "Density: %s" % density
print "<data>\r"
print "Hex  Name            UWP       Remarks                {Ix} (Ex)    [Cx]   N B  Z   PBG W  A      Stellar       \r"
print "---- --------------- --------- ---------------------- ---- ------- ------ - -- --  --- -- ------ --------------\r"

for column in range (min_column, max_column): #generate subsector
	for row in range (min_row, max_row):
		throw=dice(sector_density[0],sector_density[1])
		if throw<=sector_density[2]:    # 3 is standard density
			if row<=9:
				row_loc="0%i" % (row)
			if row>=10:
				row_loc="%i" % (row)
			if column<=9:
				column_loc="0%i" % (column)
			if column>=10:
				column_loc="%i" % (column)
			location=column_loc+row_loc
			gensys()
			totsystems=totsystems+1

print "</data>\r"
print "systems=%s" % totsystems
print "</sec>\r"
outp.write("</data>"+'\r\n')
outp.write("systems="+str(totsystems)+'\r\n')
outp.write("</sec>"+'\r\n')
outp.close()

#write config file
if realism==0:
    reality="canon"
if realism==1:
    reality="real"
if spacesize==1:
    space="subsector"
if spacesize==2:
    space="sector"
if habitation==0:
    habitation2="empty"
if habitation==1:
    habitation2="inhabited"
outp = open("gensec.conf","w")
outp.write(reality+'\r\n')
outp.write(space+'\r\n')
outp.write(habitation2+'\r\n')
outp.write(sector_name+'\r\n')
outp.write(file_name+'\r\n')
outp.write(density+'\r\n')
outp.close()
