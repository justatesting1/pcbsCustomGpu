def check(_input):
    _flag = False
    _var=""
    while not _flag:
        _var = input(_input)
        if not _var.isalpha():
            if _var == "":
                print("Enter only numbers")
            else:
                _flag=True
        else:
            print("Enter only numbers")
    return _var

_classFlag=False
while not _classFlag:
    _class=input("Choose a class (Ultra, Normal) ").lower()
    if _class == "ultra" or _class == "normal":
        _classFlag = True
    else:
        print("Choose one of the options")
_class = _class[0].upper() + _class[1:]

_man=input("Enter a manufacturer ").upper()
_id=check("Enter unique number for the GPU ")
_id="GPU_"+_man+"_"+_id
_name=input("Enter the part's name ")
_price=check("Enter the part's price ")
_sell=check("Enter the part's sell price ")
_level=check("Enter the level that it's unlocked at ")
_percentage=check("Enter percentage ")
_concat="("+_level+") " + _man + " " + _name
_chip=_name
_vram=check("Enter part's VRAM ")
_wattage=check("Enter part's wattage ")
_core=check("Enter the base core clock freq ")
_mem=check("Enter the base memory clock freq ")
_per=check("Enter the Dual GPU performance increase ")
_perS=check("Enter the Single GPU Score ")
_length=check("Enter the GPU length in mm ")
_perD=str(int(int(_perS)*float(_per)))

_sliFlag=False
while not _sliFlag:
    _sli=input("SLI? (Yes, No) (AKA Double GPUs) ").lower()
    if _sli == "yes" or _sli == "no":
        _sliFlag=True
    else:
        print("Choose one of the options")
_sli = _sli[0].upper() + _sli[1:]

_temp=check("Enter the Start Temperature ")
_throw=check("Enter the Temperature at which Thermal Throttling starts ")
_maxcore=check("Enter the max core clock freq ")
_maxmem=check("Enter the max memory clock freq ")

_light=""
_rgbFlag=False
while not _rgbFlag:
    _rgb=input("RGB? (Yes, No) ").lower()
    if _rgb == "yes" or _rgb == "no":
        _rgbFlag=True
        if _rgb=="yes":
            _light="RGB"
    else:
        print("Choose one of the options")

text="""GPU
</tr>\s+</table>
        </tr>
	<tr>
		<td div=""></td>
		<td div="Part Type">GPU</td>
		<td div="Class">"""+_class+"""</td>
		<td div="Manufacturer">"""+_man+"""</td>
		<td div="ID">"""+_id+"""</td>
		<td div="Part Name">"""+_name+"""</td>
		<td div="In Game">Yes</td>
		<td div="Imported to Game">Yes</td>
		<td div="Working in game">Yes</td>
		<td div="In Shop">Yes</td>
		<td div="Price">"""+_price+"""</td>
		<td div="SellPrice">"""+_sell+"""</td>
		<td div="Level">"""+_level+"""</td>
		<td div="Percent Through">"""+_percentage+"""</td>
		<td div="Headline"></td>
		<td div="Concat name">"""+_concat+"""</td>
		<td div="Model Supplied">No</td>
		<td div="Licensor Approved">Yes</td>
		<td div="Chipset">"""+_chip+"""</td>
		<td div="GPU Benchmark ID">"""+_chip+"""</td>
		<td div="Timeframe">Wed Mar 01 2017 00:00:00 GMT-0000 (GMT)</td>
		<td div="VRAM (GB)">"""+_vram+"""</td>
		<td div="Slot Size">Double</td>
		<td div="Wattage">"""+_wattage+"""</td>
		<td div="Length">"""+_length+"""</td>
		<td div="Score to value ratio">10</td>
		<td div="Target STV ratio">10</td>
		<td div="Base Core Clock Freq">"""+_core+"""</td>
		<td div="Base Mem Clock Freq">"""+_mem+"""</td>
		<td div="Single GPU Graphics Score">"""+_perS+"""</td>
		<td div="Double GPU Graphics Score">"""+_perD+"""</td>
		<td div="Dual GPU performance increase">"""+_per+"""</td>
		<td div="Double GPU SLI">"""+_sli+"""</td>
		<td div="Double GPU supported">"""+_sli+"""</td>
		<td div="GPU % Power Increase">20</td>
		<td div="GPU start temp">"""+_temp+"""</td>
		<td div="GPU Thermal Throttling">"""+_throw+"""</td>
		<td div="GPU max clock">"""+_maxcore+"""</td>
		<td div="GPU max mem clock">"""+_maxmem+"""</td>
		<td div="Asset Path">Prefabs/GPU/EVGA/EVGA_GTX_1080_Ti_KingPin_Gaming</td>
		<td div="Icon Path">ComponentIcons/Generic/GPU</td>
		<td div="Product Page"></td>
		<td div="Component Lighting">"""+_light+"""</td>
		<td div="Notes"></td>
		<td div="GT1 Single Core Clock Multiplier">0.02549</td>
		<td div="GT1 Single Mem Clock Multiplier">0.01673</td>
		<td div="GT1 Single Benchmark Adjustment">-9.4038</td>
		<td div="GT2 Single Core Clock Multiplier">0.02617</td>
		<td div="GT2 Single Mem Clock Multiplier">0.01563</td>
		<td div="GT2 Single Benchmark Adjustment">-15.604</td>
		<td div="GT1 Dual Core Clock Multiplier">0.04548</td>
		<td div="GT1 Dual Mem Clock Multiplier">0.03498</td>
		<td div="GT1 Dual Benchmark Adjustment">-15.202</td>
		<td div="GT2 Dual Core Clock Multiplier">0.04295</td>
		<td div="GT2 Dual Mem Clock Multiplier">0.04657</td>
		<td div="GT2 Dual Benchmark Adjustment">-38.5277</td>
	</tr>
</table>
"""

bat="""
@echo off
cls
echo Applying mod patch...
cd unitypatcher
SET "PATH="
SET /P "PATH=>"
echo Type the PC Building Simulator path and press enter. Use DOUBLE slashes (\\) or it won't work!
pause
SET "PCBSPATH=%PATH%"
echo -------------------------
call unitypatcher patch %PATH%\\PCBS_Data\\sharedassets1.assets "..\_"""+_name+""".asset.txt"
echo If patching was successful you can run the game now!
echo -------------------------
pause
"""

file=open("_"+_name+".asset.txt","w+")
file.write(text)
file.close()
_file=open(_name+".bat","w+")
_file.write(bat)
_file.close()
