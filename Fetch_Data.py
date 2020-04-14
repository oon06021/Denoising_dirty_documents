##데이터를 받을 폴더에 Fetch_Data.py 파일을 다운받고 
##Anaconda prompt 에서  python Fetch_Data.py 입력 후 엔터

conda install requests

import requests

test_url = 'https://k.kakaocdn.net/dn/bFvix1/btqDiGxBP3H/8YrhvZb6oyomwdQvFZRRR0/test.zip?attach=1&knm=tfile.zip'
train_cleaned_url = 'https://k.kakaocdn.net/dn/bLEltV/btqDkAwtxMN/g8lrXy5ACYiXzG9hAkLi50/train_cleaned.zip?attach=1&knm=tfile.zip'
train1_url = 'https://k.kakaocdn.net/dn/biFTCp/btqDje8LwJq/Nsk90EPjV77rDSbJZz3EW0/train1.zip?attach=1&knm=tfile.zip'
train2_url = 'https://k.kakaocdn.net/dn/rOqax/btqDiGxBWOn/xb3It6FhqbqeDxxTvEXAi1/train2.zip?attach=1&knm=tfile.zip'


file1 = requests.get(test_url, allow_redirects=True)
open('test.zip', 'wb').write(file1.content) #위 url 에서 받은 zip 파일을 test.zip 이라는 이름으로 받아준다. 아래도 쭉 같은 논리

file2 = requests.get(train_cleaned_url, allow_redirects=True)
open('train_cleaned.zip', 'wb').write(file2.content)

file3 = requests.get(train1_url, allow_redirects=True)
open('train1.zip', 'wb').write(file3.content)

file4 = requests.get(train2_url, allow_redirects=True)
open('train2.zip', 'wb').write(file4.content)

print("모든 파일이 다운로드 되었습니다.")
