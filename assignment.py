import numpy
import math
print("\n\t**********Code for NETWORK AND SECURITY Assignment**********")
Roll_str=input("\nEnter your Roll Number: ")
print("\n\t**********Solution for assignment question 2**********")
#Converting the string Roll Number to Integer List
Roll_Number=[]
for i in range(0,len(Roll_str)):
    Ro=int(Roll_str[i])
    Roll_Number.append(Ro)
one_star=Roll_str[-1]
two_star=Roll_str[-2]+Roll_str[-1]
three_star=Roll_str[-3]+Roll_str[-2]+Roll_str[-1]
#Converting the string Roll Number to Hexadecimal List
Roll_Number_hex=[]
for i in range(0,len(Roll_str)):
    Ro=int(Roll_str[i],16)
    Roll_Number_hex.append(Ro)
#Obtaining Binary of last digit
last_digit=bin(Roll_Number_hex[-1])
#Creating the message data
if len(last_digit)>=6:
    message="11"+last_digit[2:6]
else:
    if len(last_digit[2:6])==3:
        message="110"+last_digit[2:6]
    elif len(last_digit[2:6])==2:
         message="1100"+last_digit[2:6]
    else:
        message="11000"+last_digit[2:6]
print("\nMessage data for given parameters: ", message)
#Creation of divisor bit
#Applying Bit wise Exor to find sum of the Roll Number
for i in range(0,len(Roll_Number_hex)):
    if i==0:
        exor=Roll_Number_hex[i]
    else:
        exor=exor^Roll_Number_hex[i]
roll_sum=bin(exor)
def xor(a, b):
    xor_res = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            xor_res+='0'
        else:
            xor_res+='1'
    return xor_res
#Funtion for performing modulo-2 division
def mod2div(dividend,divisor):
    pick=len(divisor)
    tmp=dividend[0:pick]
    while pick<len(dividend):
        if tmp[0]=='1':
            tmp=xor(divisor,tmp)+dividend[pick]
        else:
            tmp=xor('0'*pick,tmp)+dividend[pick]
        pick+=1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword
#Function to encode the message
def encodeData(data,key):
    keylen=len(key)
    appended_data=data+'0'*(keylen-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword
#Forming the codeword
key='1101'
ans=encodeData(message,key)
print("The reminder of modulo-2-division is: ",ans[-3:len(ans)])
print("The transmitted code word is: ", ans)

#Third question
print("\n\t**********Solution for Assignment 3**********")
Speed_of_light=300000
#Calculation of Message size
msg_size_inkb=float("2."+str(exor))
msg_size=msg_size_inkb*1000
print("\nThe Message size of the Given data is: ", msg_size)
#Calculation of Bandwidth
bw_ingbps=float("1."+two_star)
bw=bw_ingbps*1000000000
print("Bandwidth of the Given Input data: ",bw)
#Calculation of Distance
dis_last=str(Roll_Number[-3])+str(Roll_Number[-2])+str(Roll_Number[-1])
distance=int("12"+dis_last)
print("Distance between the sender and reciever: ", distance)
#calculation of propagation time
propa_time=distance/Speed_of_light
print("The propagation time taken in the given network is: ",propa_time,' sec')
#calculation of transmission time
trans_time=msg_size/bw
print("The transmission time for the given message and bandwidth is: ",trans_time,' sec')

#Fourth question
print("\n\t**********Solution for Fourth question Second sub-division**********")
#Assigning the IP
if exor<=9:
    hashval=str(exor)
else:
    hashtemp=str(exor)
    hashval=str(int(hashtemp[0])+int(hashtemp[1]))
ip1="1"+one_star+"4."+'34.'+'2.'+two_star
ip2='13'+hashval+'.'+two_star+'.8.'+hashval
ip3='2'+two_star+'.34.'+two_star+'.12'
print("\nThe first IP Address for the given data: ",ip1)
print("The second IP Address for the given data: ",ip2)
print("The third IP Address for the given data: ",ip3)
#Creating a fuction to find the Class of IP
def classofip(ip):
    print("\nThe given ip",ip,":")
    ip_list=ip.split('.')
    first8=int(ip_list[0])
    if first8<=127:
        print("The address is Class A")
        print("Network ID: ",ip_list[0])
        print("Host ID: ",ip_list[1]+'.'+ip_list[2]+'.'+ip_list[3])
    elif first8<=191:
        print("The address is Class B")
        print("Network ID: ",ip_list[0]+'.'+ip_list[1])
        print("Host ID: ",ip_list[2]+'.'+ip_list[3])
    elif first8<=223:
        print("The address is Class C")
        print("Network ID: ",ip_list[0]+'.'+ip_list[1]+'.'+ip_list[2])
        print("Host ID: ",ip_list[3])
    elif first8<=239:
        print("The address is Class D")
    else:
        print("The address is Class E")
#calling the function
classofip(ip1)
classofip(ip2)
classofip(ip3)

#Fifth question
print("\n\t**********Solution for Fifth Question**********")
bw1=(int('1'+one_star))*1000
snrdb1=int('2'+str(exor))
bw2=(int('15'+one_star))*1000
snrdb2=8
bw3=2000000
snrdb3=int('1'+one_star)
def calcofc(Bw,snrdb):
    snr=10**(snrdb/10)
    templog=1+snr
    logans=math.log2(templog)
    Capacity=Bw*logans
    print("\nBandwidth of the given channel is: ",Bw,' Hz')
    print("Signal-to-noise ratio of the given channel is: ",snr)
    print("The theroretical capacity of the channel is: ",Capacity,' bps')
calcofc(bw1,snrdb1)
calcofc(bw2,snrdb2)
calcofc(bw3,snrdb3)

#Seventh question
speed_s=2.5*100000000
length_l=int('1'+two_star)
bw_r=int('2'+hashval)
print("\n\t**********Solution for seventh question**********")
print("\nSpeed of propagation: ",speed_s,'m/s')
print("size of the given data: ",length_l,' bits')
print("Bandwidth of the transmission link: ",bw_r,'kbps')
Distance_m=(length_l*speed_s)/(bw_r*1000*1000)
print("The distance between sender and reciever so that dtrans and dprop are same is ",Distance_m,' km')

#Eighth question
print("\n\t**********Solution for Eighth question**********")
bw_8=float('1.'+three_star)
total_data_packets=(2**32)*320
wrap_around=total_data_packets/(bw_8*1000000000*60)
print("\nThe time taken for the sequence to completely wrap around is: ",wrap_around,' mins')
increment=int('1'+three_star)
wrap_around_factor=4*1000000000/increment
WA_timestamp=wrap_around_factor*wrap_around/(60*24*365)
print("The time taken for the timestamp ffield to wrap around when there is a increment of ",increment, "is: ",WA_timestamp)
