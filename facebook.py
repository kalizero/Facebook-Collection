__author__ = 'toannd11'

import requests
import threading
import json
import base64
import urllib2
import datetime
import time

def api_getinfo(code, phone_first, phone_last,cl_facebook,headers_value,count, notfound):
    for phone in range(phone_first, phone_last):
        phone = code+str(phone)
        count = count +1
        thread_name = threading.current_thread().name
        print "Thread: "+thread_name+" has request: "+str(count)
######################Check phone exist#################################
#        phone_exist = cl_facebook.find({"phone":phone}).count()
	phone_exist = 0
        if phone_exist < 1:
            url = 'https://api.facebook.com/method/ubersearch.get?include_native_ios_url=true&support_groups_icons=true&group_icon_scale=2&context=mobile_search_ios&limit=10&locale=en_US&sdk_version=3&photo_size=64&filter=%5B%27user%27%2C%27page%27%2C%27group%27%2C%27event%27%2C%27app%27%2C%27hashtag_exact%27%2C%20%27shortcut%27%5D&query='+phone+'&fb_api_caller_class=FBSimpleSearchTypeaheadRequest&sdk=ios&fb_api_req_friendly_name=ubersearch&include_is_verified=true&uuid=C67598DE-22BA-443C-AE71-E6693BE8FE9E&app_version=4463064&format=json'
            header = headers_value
            try:
                time.sleep(2)
                r = requests.get(url, headers = header)
                result = r.text
                print result
                leng = len(result)
                if (leng < 3):
                    notfound = notfound +1
                    print "The "+phone+" not found: "+str(notfound)

                    if (notfound > 25):                        # if find phone not found 25 time then sleep
                        hour = 60*40
                        time_sleep = datetime.datetime.now()
                        print "#############################"
                        print time_sleep
                        print "#############################"
	                time.sleep(hour)
			notfound = 0
                    else:
                        pass
                else:
                    notfound = 0
                    result = json.loads(result)
            except Exception, e:
                pass
            try:
                for item in result:
                    if item['uid']:
                        userid = item['uid']
                        print "______________________________________________________________"
                        print "Phone number: "+phone
                        print "User id: "+userid
                        name_text = item['text']
                        print "Name face: "+name_text
                        photos = item['photo']
                        print "Link photos: "+photos
                        user_path = item['path']
                        print "user path: "+user_path
                        try:
                            if not 'category' in item:
                                category = 'null'
                                print "Category: "+category
                                pass
                            else:
                                category = item['category']
                                print "Category: "+category
                        except Exception,e:
                            pass
# Insert value to db
                        print "______________________________________________________________"
                        url = photos
                        photo = urllib2.urlopen(url)
                        image = photo.read()
                        image_base64 = base64.b64encode(image)
                        '''
                        image_binary = bson.Binary(image)
                        print(image_binary)
                        image_ded = base64.b64decode(image_base64)
                        image = open('test.jpg','w')
                        image.write(image_binary)
                        image.close()

                        user_id = cl_facebook.find({"userid":userid}).count()
                        print user_id
                        if user_id < 1:
                        '''
                        cl_facebook.insert({"phone": phone, "category": category, "userid": userid, "name": name_text,"image": image_base64, "path": user_path})
                    else:
                        print "The phone number "+phone+" not found"
            except Exception, e:
                pass
        else:
            print "The number "+phone+" Existed:"
