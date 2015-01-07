__author__ = 'toannd11'

import pymongo
import facebook
import threading

#https://www.facebook.com/search/web/direct_search.php?q=0965618100
# https://www.facebook.com/search/results/?q=0976765888
# https://www.facebook.com/search/more?q=0965618100
#1800 usa verizon celler
################# Connect to mongodb ##########################################################################
connection = pymongo.Connection("localhost", 27017)
db = connection['contact']
cl_facebook = db.facebook

################Define Attribute###############################################################################
# ischeck = 0 >> not check
# ischeck = -1 >> checked facebook not foud
# ischeck = -2 >> checked Zalo not foud
# ischeck = -3 >> checked viber not foud
# ischeck = -4 >> checked

# ischeck = 1 >> checked facebook not foud
# ischeck = 2 >> checked Zalo not foud
# ischeck = 3 >> checked viber not foud
# ischeck = 4 >> checked ...
#################End Attribute###################################################################################
# set count number request to facebook
cout = 0
notfound = 0
user_agent = ",'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 [FBAN/FBIOS;FBAV/15.0.0.16.28;FBBV/4463064;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.1.2;FBSS/2; FBCR/FBID/phone;FBLC/en_US;FBOP/5]'"
#################List cookie#####################################################################################
#url = 'https://api.facebook.com/method/ubersearch.get?include_native_ios_url=true&support_groups_icons=true&group_icon_scale=2&context=mobile_search_ios&limit=10&locale=en_US&sdk_version=3&photo_size=64&filter=%5B%27user%27%2C%27page%27%2C%27group%27%2C%27event%27%2C%27app%27%2C%27hashtag_exact%27%2C%20%27shortcut%27%5D&query='+phone+'&fb_api_caller_class=FBSimpleSearchTypeaheadRequest&sdk=ios&fb_api_req_friendly_name=ubersearch&include_is_verified=true&uuid=C67598DE-22BA-443C-AE71-E6693BE8FE9E&app_version=4463064&format=json'
header_nguyenvanthienthien1 = {'Authorization':'OAuth CAAAAUaZA8jlABANho1rWyOdhi4Kra4Yo7KbY4CCwaGGxoarGiuHLRZArMLm5hZAXssZBPkz1n0Ldn4j0oyc22G65HmizS15c6BANKUZCZCNTddjUL0cwj9OycwLCyZCXSwmpCA6QWVIOsbnZBI6iTNRErFJ3nUr5wyp4P5va8Kyc4BIZATeE3TixaD137re5jKZAIMZD'+user_agent}
header_hathithuhuonghuong = {'Authorization':'OAuth CAAAAUaZA8jlABANgqT3oxUuxks83FTclBjGemGC5klnZA84tO8hiVp0ZCQSYBu18UVXKs5HjaNgceq0mMx2e2tinE6sZBrRFKyQEH0GibitWVi2HrzcpC3eIlVrhn9FR6IhcbKZCSwir9McdGtPAA758smvH3fQWqT0SmeVEV7MBe3Ynd0OyDa1ZB8UUQ1I5uoZD'+user_agent}
header_dangtiendongboyy = {'Authorization':'OAuth CAAAAUaZA8jlABAAtNDs1XfUv7AhEdS5UkNJSfLRr9C9aY0BrTI7TSXk6omz1z1M1ZCmZBspZCTxR8I5ZB5c66ECDZBAhhy3jyDfT6cEleYZCYp6m29ZB82ZAbAWzuS3S6ZBzsOqwZBKPVUgoynp5LbOLZB2odcI1fqMoVs2ZAqaSPtyOKCaBLZCxG3G0EwsRvfGMJOPVzAZD'+user_agent}
header_namhanhnamm = {'Authorization':'OAuth CAAAAUaZA8jlABAGl1Ni31P4ZAz692spWfB0DGwaBdZCqkp8N0Q6oTZBw4gTZChFAHbsWcBqa3RasXYDHf6xZC7CcKnkjurNuddSgPBJMzeGqKERBewm3ZCqDqN40ZA8mkcXeslDPAjKLAHJ4RZCWWSZCptEH2RPH0YCTojbcIevNWPEZBIcno7ueBJNa'+user_agent}
header_giangmanhgiangg = {'Authorization':'OAuth CAAAAUaZA8jlABAOMGqpb2xT0Ak9yqOUsbwYf9FJt75ScDxpU26R0ByX0lzEgkOPtjLofKxyVsVL5qsA42rZAAvtTGz951ZAweKxluZAcCu5Y4lZBuLPNeY8B57dIpvrVW9QBZAkkycmQQvdfZBC1ZBRXJdHHIj7DbMnwnya6xX41LfnyMVRlefLsE72eNzeSZAeSsZD'+user_agent}
header_hoangxuanhuongg = {'Authorization':'OAuth CAAAAUaZA8jlABADWG9sbLVLRvPiYFQPJunZCLhLEcR9er0ZAY6dK3g1nRCdQRlPUAe6R4dcenqnE6xuzvzQBT0kmUpBoH6VM59d5TNU73OZCXvtdM5ZCS2BRPQzli21YXr9NkSkRkD5cKU3bKFD4tKuBt4qUXkds22VagGPLTniRT9ovNTSre'+user_agent}
header_khaihoanghuongg = {'Authorization':'OAuth CAAAAUaZA8jlABAKpZAXi7ZB7sQ7Y75ZAsiZAIibzxtoUDlOayZAAzxYGIRBOUGuJ3pxDKywSsxs13kv3xpDUkZAPSo4Xwiiiqwd0QHWRGMFYQJ8HI9HEZCHuMgER6K12pNvajFJLzVaAirQ8xQugZBZAPVxUuRYMOrwMShVfWw8W02x0j16x8CpdSE0'+user_agent}
header_cuongkiencuongg = {'Authorization':'OAuth CAAAAUaZA8jlABAHSzIHIUFDtq10AVWSkJFNxSBfWSVi4JcFtn9ivW0EWS9yzzixUYxjOlL7msfZCiL9gZApa0uWzO4yfU9ZCAeXhq8ScJ0ZCsoGgfYEjKkwgx7Ap0x2ddtNW4FT62bskwBUSr8QriRgbuZCpMDyXm4XgsrigHE3JZBVCoNL02j9v10j9a5ZBhCIQZD'+user_agent}
header_quankiencuongg = {'Authorization':'OAuth CAAAAUaZA8jlABAHbOFPTro2iOak9Y16vzfRTLrpZAThf2jpsRAiMlXwDr1m5m3jC7hDbCqzZCsZASgom2HDi6p861zA5R4mjvrKZB3LgMQ8Jsrh5QCnNXeCWwEMYPWZA6jn4wmjhPm13msoz0NQ3csYxh7iUKt4fZB1V4ZCvExxd80ZALJn8m1iCqy'+user_agent}
header_toan = {'Authorization':'OAuth CAAAAUaZA8jlABAAKiJ83Hfu06npNeBryZCx01TqbOupMVUx8q7wBUYFAKfKYpZAncGWZCNCkCSwnLm52ZA9JesnZBxPufkrKSgPGgKgVfMQbRw4pvjsi0Lx81PZB7KoKmkfaih19Dl3F1LZCEaBI18kZBrmKaNc9N6ZAIZC8zZB9ZBIUuCgNfI4ZAPNvCCDmh5adASKE9Ipb2F9MosUXNvIPOfw4nBN'+user_agent}

header_dic = {"header_namhanhnamm":header_namhanhnamm,"header_nguyenvanthienthien1":header_nguyenvanthienthien1,"header_hathithuhuonghuong":header_hathithuhuonghuong,"header_giangmanhgiangg":header_giangmanhgiangg,
              "header_hoangxuanhuongg":header_hoangxuanhuongg,"header_khaihoanghuongg":header_khaihoanghuongg,"header_cuongkiencuongg":header_cuongkiencuongg,"header_dangtiendongboyy":header_dangtiendongboyy, "header_quankiencuongg":header_quankiencuongg,"header_toan":header_toan}
#################End list cookie#################################################################################

##############Define list phone to search#######
code = '84'
phone_nguyenvanthienthien1 = "84983"
phone_hathithuhuonghuong = "84984"
phone_dangtiendongboyy = "84985"
phone_namhanhnamm = "84986"
phone_giangmanhgiangg = "84987"
phone_hoangxuanhuongg = "84988"
phone_khaihoanghuongg = "84989"
phone_cuongkiencuongg = "84902"
phone_quankiencuongg = "84903"
phone_toan = "84904"
phone_list = [phone_nguyenvanthienthien1,phone_hathithuhuonghuong,phone_namhanhnamm,phone_giangmanhgiangg,phone_hoangxuanhuongg,phone_khaihoanghuongg,phone_cuongkiencuongg, phone_dangtiendongboyy, phone_quankiencuongg, phone_toan ]
lengs = len(phone_list)
##############End list phone####################

################# Get last phone number inserted on db############################################################
def get_firstphone(phones):
    #i = cl_facebook.find({phone => qr/^phones/},{"phone":1, "_id":0}).skip(cl_facebook.count() -1)
    a = cl_facebook.find({"phone":{"$regex":"^"+phones}},{"phone":1, "_id":0})
    b = cl_facebook.find({"phone":{"$regex":"^"+phones}},{"phone":1, "_id":0}).count()
    if (b < 1):
        phones = phones+"000000"
        cl_facebook.insert({"phone": phones, "category": "null", "userid": "null", "name": "null","image": "null", "path": "null"})
        print "Insert phone: "+phones
    else:
        y = a.skip(b -1)
        for phone in y:
            phone = str(phone['phone'])
            phone = phone.replace("84","",1)
            phone = int(phone)
    return phone

###################Get last phone#################################################################################
def get_lastphone(phones):
    phone_first = get_firstphone(phones)
    phone_last = int(str(phone_first)[:3]+"999999")
    return phone_last

##################Run instant thread##########################
header_key = []
header_value =[]
threads = []
for hkey, hvalue in header_dic.iteritems():
   header_key.append(hkey)
   header_value.append(hvalue)
for i in range(lengs):
    phone = phone_list[i]
    phone_first = get_firstphone(phone)
    phone_last = get_lastphone(phone)
    headers_key = header_key[i]
    headers_value = header_value[i]

    t = threading.Thread(name=headers_key,target=facebook.api_getinfo, args=(code, phone_first, phone_last,cl_facebook,headers_value,cout, notfound))
    threads.append(t)
    t.start()

#facebook1.api_getinfo(code,phone0,phone9,cl_facebook)

