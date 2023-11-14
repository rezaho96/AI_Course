str1='''
Name:Ahmad,Family:Ghaderi,Mobile:09123458765,Postal Code:1417466191,city:Tehran,Mailing Address: No.29, Ardeshir Alley, Hashtbehesht St., Golha Square, Dr. Fatemi St.
Name:Zahra,Family:Miraee,Mobile:09367006534,Postal Code:1115586391,city:Tehran,Mailing Address:No.18, 4th Bahman St., North Kanal Ab St., Khavaran Rd., Khatoun Abad.
Name:Ziba,Family:Nalbandi,Mobile:09356546534,Postal Code:3185679365,city:Karaj,Mailing Address:No.49,Razi St., Haft_e_Tir crossroad.
Name:Babak,Family:Naimee,Mobile:09121235678,Postal Code:1996715433,city:Tehran,Mailing Address:No.45,Emam Khomaini Square, Khayam st.Shahid Fayaz Bakhsh st.
Name:Fatemeh,Family:Moradi,Mobile:09133047777,Postal Code:8174673441,city:Isfahan,Mailing Address:No. 510, 3rd Fl., Kowsar Trading Complex, Beginning of Chahar Bagh Bala. 
Name:Ahmad,Family:Akbari,Mobile:09123124455,Postal Code:1587544133,city:Tehran,Mailing Address:No.51, Safi Alley, Sattar Khan Ave., Tohid Sq.
Name:Reza,Family:Rafiee,Mobile:09121446216,Postal Code:3225639365,city:Tehran,Mailing Address:No. 5, Niam St., Dr. Shariati Ave.
Name:Hossien,Family:Saai,Mobile:09130123993,Postal Code:8165673242,city:Isfahan,Mailing Address:No. 132, Azadi St., Hezar Jarib St. 
Name:Asghar,Family:Hossaini,Mobile:09131170730,Postal Code:8171663343,city:Isfahan,Mailing Address:No. 159, Mir St.
Name:Masoud,Family:Sorami,Mobile:09122122962,Postal Code:1465865163,city:Tehran,Mailing Address:No.26, Tavanir Ave., Vali-e-Asr Ave.
Name:Amir,Family:Hajamini,Mobile:09121303804,Postal Code:1585988713,city:Tehran,Mailing Address:No.5,Farivar Alley, Ghaem Magham Street.
Name:Lida,Family:Abedi,Mobile:09142418085,Postal Code:5166616471,city:Tabriz,Mailing Address:No.47, Kamyar, Takhti St. Valiasr. 
Name:Babak,Family:Hamedi,Mobile:09141149921,Postal Code:5163315441,city:Tabriz,Mailing Address:No.21 St. Salimi Industrial town. 
'''
import re
import os
regex_info=re.findall(r"(.+,Family:.+,Mobile:0912\d{7}.+city:.+?),",str1)
print(regex_info)
print(os.getcwd())
# save in file
with open("Homework/info_0912.csv","w") as file1:
    for item in regex_info:
        file1.write(item+"\n")

