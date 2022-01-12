from sqlite3.dbapi2 import connect
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import dbconn

wiz_url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='
slide_num = 1
parser = argparse.ArgumentParser()
parser.add_argument("--search_to_page", help="Enter the number of sites to explore", type=int)
parser.add_argument("--dbname", help="Enter the naame of database to connect", type=str)
args = parser.parse_args()

scrapped_info_list = []
dbconn.connect(args.dbname)

for i in range(args.search_to_page): # range size will change if more pages will add to site
    req = requests.get(wiz_url + f'{slide_num}')
    content = req.content


    soup = BeautifulSoup(content, "html.parser")
    all_mobiles = soup.find_all("div", {"class": "_13oc-S"})
    # print(all_mobiles)
    for mobiles in all_mobiles:
        mobile_dict = {}
        try:
            mobile_dict["name"] = mobiles.find("div", {"class": "_4rR01T"}).text
        except AttributeError:
            mobile_dict["extra"] = "Not given yet"
        try:
            mobile_dict["price"] = mobiles.find("div", {"class": "_30jeq3"}).text
        except AttributeError:
            mobile_dict["extra"] = "Not given yet"
        try:
            mobile_dict["specifictions"] = mobiles.find("ul", {"class": "_1xgFaf"}).text
        except AttributeError:
            mobile_dict["extra"] = "Not given yet"
        try:
            mobile_dict["rating"] = mobiles.find("div", {"class": "_3LWZlK"}).text
        except AttributeError:
            mobile_dict["extra"] = "Not given yet"
        try:
            mobile_dict["reviews"] = mobiles.find("span", {"class": "_2_R_DZ"}).text
        except AttributeError:
            mobile_dict["extra"] = "Not given yet"
        # print(mobile_dict)
        scrapped_info_list.append(mobile_dict)

    slide_num += 1
    dbconn.insert_into_table(args.dbname, tuple(mobile_dict.values()))

dataFrame = pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv('Mobile.csv')
dbconn.get_mobile_info(args.dbname)
print("DataBase and Excel file created")
print("Program succesfully Terminated")