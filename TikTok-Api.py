#Api was extracted by the programmer [ M3GON ]
#Instagram : @_m3gon
#Telegram : @M3GONPY
import requests
def change_nickname():
    #Enter Here Sessionid Your Account In TikTok
    sessionid_your_account = ''

    #Enter NickName New
    NickName = ''

    #Url Change NickName
    url_change_nickname = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?version_code=7.7.0&language=ar&app_name=musical_ly&vid=CFC622B3-1BCA-415A-9F89-3F28B1CCC10E&app_version=7.7.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6964994583017539077&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=885379c6a0b17fb611f881639c8be5f066228116&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=77003&device_type=iPhone10,6&iid=6966925701539645190&idfa=00000000-0000-0000-0000-000000000000&mas=01e7eb5e69512143bef888baed95be973306fd005bb278627328d8&as=a146070a731480be1f7267&ts=1622113859'

    #Headers Change NickName
    headers_change_nickname = {
        'Host': 'api2-t2.musical.ly',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
        'Content-Length': '19',
        'Connection': 'close',
    }

    #Cookies Change NickName
    cookies_change_nickname = {'sessionid': sessionid_your_account}

    #Data Change NickName
    data_change_nickname = f'nickname={NickName}'

    #Request Change NickName
    response_change_nickname = requests.post(url_change_nickname, data=data_change_nickname, cookies=cookies_change_nickname, headers=headers_change_nickname).text
change_nickname()
#============================================================================================
def change_bio():
    #Enter Here Sessionid Your Account In TikTok
    sessionid_your_account = ''

    #Enter New Bio Here
    Bio = ''

    #Url Change Bio
    url_change_bio = 'https://api2-t2.musical.ly/aweme/v1/commit/user/?version_code=7.7.0&language=ar&app_name=musical_ly&vid=CFC622B3-1BCA-415A-9F89-3F28B1CCC10E&app_version=7.7.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6964994583017539077&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=885379c6a0b17fb611f881639c8be5f066228116&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=77003&device_type=iPhone10,6&iid=6966925701539645190&idfa=00000000-0000-0000-0000-000000000000&mas=01e7eb5e69512143bef888baed95be973306fd005bb278627328d8&as=a146070a731480be1f7267&ts=1622113859'

    #Headers Change Bio
    headers_change_bio = {
        'Host': 'api2-t2.musical.ly',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
        'Content-Length': '19',
        'Connection': 'close',
    }

    #Cookies Change Bio
    cookies_change_bio = {'sessionid': sessionid_your_account}

    #Data Change Bio
    data_change_bio = 'signature=TestChangeBio'

    #Request Change Bio
    response_change_bio = requests.post(url_change_bio, data=data_change_bio, cookies=cookies_change_bio, headers=headers_change_bio).text
change_bio()
#============================================================================================
def like_video():
    #Enter Here Sessionid Your Account In TikTok
    sessionid_your_account = ''

    #Enter Here Id Vidoe TikTok
    id_video = ''

    #Url Like Video
    url_like_video = 'https://api2-19.musical.ly/aweme/v1/commit/item/digg/?version_code=7.7.0&language=ar&app_name=musical_ly&vid=CFC622B3-1BCA-415A-9F89-3F28B1CCC10E&app_version=7.7.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6964994583017539077&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=885379c6a0b17fb611f881639c8be5f066228116&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=77003&device_type=iPhone10,6&iid=6966925701539645190&idfa=00000000-0000-0000-0000-000000000000&mas=01c51404d132dfc2940fcea7b455c44104e2b9f2fdf04cbf6ea0c1&as=a1f6a82ac3c4c062ff4776&ts=1622114883'

    #Headers Like Video
    headers_like_video = {
        'Host': 'api2-19.musical.ly',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
        'Content-Length': '19',
        'Connection': 'close',
    }

    #Cookies Like Video
    cookies_like_video = {'sessionid': sessionid_your_account}

    #Data Like Video
    data_like_video = f'aweme_id={id_video}&type=1'

    #Request Like Video
    response_like_video = requests.post(url_like_video, data=data_like_video, cookies=cookies_like_video, headers=headers_like_video).text
like_video()
#============================================================================================
def send_comment():
    #Enter Here Sessionid Your Account In TikTok
    sessionid_your_account = ''

    #Enter Here Id Vidoe TikTok
    id_video = ''

    #Enter Text Or Comment Here
    Text_Or_Comment = ''

    #Url Send Comment
    url_send_comment = 'https://api2-t2.musical.ly/aweme/v1/comment/publish/?version_code=7.7.0&language=ar&app_name=musical_ly&vid=CFC622B3-1BCA-415A-9F89-3F28B1CCC10E&app_version=7.7.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6964994583017539077&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=885379c6a0b17fb611f881639c8be5f066228116&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=77003&device_type=iPhone10,6&iid=6966925701539645190&idfa=00000000-0000-0000-0000-000000000000&mas=018b53a1c977079483e02e7267252a5ec22b2b2d454de0a334deb8&as=a136b8aa2c10806e9f0908&ts=1622117900'

    #Headers Send Comment
    headers_send_comment = {
        'Host': 'api2-t2.musical.ly',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
        'Content-Length': '19',
        'Connection': 'close',
    }
    #Cookies Send Comment
    cookies_send_comment = {'sessionid': sessionid_your_account}

    #Data Send Comment
    data_send_comment = f'aweme_id={id_video}&text={Text_Or_Comment}'

    #Request Send Comment
    response_send_comment = requests.post(url_send_comment, data=data_send_comment, cookies=cookies_send_comment, headers=headers_send_comment).text
send_comment()
#============================================================================================
def search_username():
    #Enter Here Sessionid Your Account In TikTok
    sessionid_your_account = ''

    #Enter Here Username To Search
    Username = ''

    #Url Search Username
    url_search_username = f'https://api2-t2.musical.ly/aweme/v1/discover/search/?version_code=7.7.0&language=ar&app_name=musical_ly&vid=CFC622B3-1BCA-415A-9F89-3F28B1CCC10E&app_version=7.7.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6964994583017539077&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=885379c6a0b17fb611f881639c8be5f066228116&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=77003&device_type=iPhone10,6&iid=6966925701539645190&idfa=00000000-0000-0000-0000-000000000000&count=20&cursor=0&keyword={Username}&search_source=discover&type=1&mas=01a06fee84c301fe74daa4a1bbfa851590b6b76cfe1e142363628e&as=a136a90a2d50f031ff1035&ts=1622118669'

    #Headers Search Username
    headers_search_username = {
        'Host': 'api2-t2.musical.ly',
        'Accept': '*/*',
        'User-Agent': 'Musically/7.7.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, ars-SA;q=0.9, en-GB;q=0.8, en-SA;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close'
    }

    #Cookies Search Username
    cookies_search_username = {'sessionid': sessionid_your_account}

    #Request Search Username
    response = requests.get(url_search_username, cookies=cookies_search_username, headers=headers_search_username).text
search_username()
