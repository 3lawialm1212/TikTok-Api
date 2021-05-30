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
    data_change_bio = f'signature={Bio}'

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
    response_search_username = requests.get(url_search_username, cookies=cookies_search_username, headers=headers_search_username).text
search_username()
#============================================================================================
def reset_password_with_email():
    #Enter Here Email To Reset Password
    email = ''

    #Url Reset Password
    url_reset_password = 'https://api2-19.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=8.1.0&language=ar&app_name=musical_ly&vid=DE94C75B-4453-4631-B767-F13EC82F2533&app_version=8.1.0&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6904193135771207173&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=3304102db83845f858f877479059fb754854080c&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=81005&device_type=iPhone10,6&iid=6952419388407727877&idfa=D78BAC01-848D-4371-A604-7C3F3D678058&mas=01565e5bd5fc7c45ca0dbfaf0b431797810a9b3cfde417b2d50ebe&as=a1a6df67780d2014cb9003&ts=1618736344'

    #Headers Reset Password
    headers_reset_password = {
        'Host': 'api2-19.musical.ly',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'store-country-code=sa; store-idc=alisg; cmpl_token=AgQQAPO_F-RPsI4vzNb-op0_xbEGIBnKf4c0YPgypQ; d_ticket=ef487f804c448df92b74cb66c549aacbea3a4; multi_sids=6778236784885122054%3A5924bd520531b0737f82a92b735cf080; odin_tt=0140fc78f3b9071a0785ce4bfa54c3fd77c077d617adec9e5e41761d34bb06098b245296db51a9de64ac9d35e94faabe8655ff3fd8a5611cc8d03c634598170e; sessionid=5924bd520531b0737f82a92b735cf080; sessionid_ss=5924bd520531b0737f82a92b735cf080; sid_guard=5924bd520531b0737f82a92b735cf080%7C1618733832%7C5184000%7CThu%2C+17-Jun-2021+08%3A17%3A12+GMT; sid_tt=5924bd520531b0737f82a92b735cf080; uid_tt=0775db38e7839f91938e510ed8e67f104c8a987f03cc1b2ce7c240f9699b615c; uid_tt_ss=0775db38e7839f91938e510ed8e67f104c8a987f03cc1b2ce7c240f9699b615c; passport_csrf_token=b4bdeaf659414f4f84a445d2fbd579d8; passport_csrf_token_default=b4bdeaf659414f4f84a445d2fbd579d8; install_id=6952406605603538694; ttreq=1$d88452a4db1211412e4f7c92b77a41f0c4dd513a',
        'Connection': 'close',
        'Accept': '*/*',
        'User-Agent': 'TikTok/8.1.0 (iPhone; iOS 14.2; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1, en-SA;q=0.9',
        'Content-Length': '33',
        'Accept-Encoding': 'gzip, deflate'
    }

    #Data Reset Password
    data_reset_password = f'email={email}'

    #Request Reset Password
    response_reset_password = requests.post(url_reset_password, data=data_reset_password, headers=headers_reset_password).text
reset_password_with_email()
