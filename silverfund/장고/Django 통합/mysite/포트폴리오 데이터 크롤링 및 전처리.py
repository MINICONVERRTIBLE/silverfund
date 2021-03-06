#!/usr/bin/env python
# coding: utf-8

# In[14]:


#8분류 데이터 수집
#1,2번 셀에서 download.default_directory 경로만 상대경로로 수정이 안된다

from selenium import webdriver
import time
import os
from datetime import datetime

current_time = datetime.now()
Year = str(current_time.year)
Month = str(current_time.month)
if len(Month)==1:
    Month=str(0)+Month
Day = str(current_time.day)
if len(Day)==1:
    Day=str(0)+Day
Today=Year+Month+Day #오늘날짜를 8자리 숫자로 표현, 다운받을시 파일명에 포함됨

def DeleteAllFiles(filePath): # 파일이 저장될 디렉토리에 기존 파일이 존재한다면 삭제해주는 함수
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

file_path = './static/8분류'
DeleteAllFiles(file_path)

options = webdriver.ChromeOptions()

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
options.add_argument('user-agent=' + user_agent)

options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.

options.add_experimental_option("prefs", {'download.default_directory':r'C:\Users\pc\OneDrive\바탕 화면\Django\mysite\static\8분류'})#파일저장 경로 설정

chromedriver = './static/chromedriver.exe'
driver = webdriver.Chrome(chromedriver, options=options)

driver.get('https://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/cmpann/DISPensionProfit.xml&divisionId=MDIS01010003000000&serviceId=SDIS01010003000#!')
time.sleep(5)

#주식 국내 연금저축, Xpath를 활용한 클릭 방식으로 필요한 자료 다운로드
driver.find_element_by_xpath('//*[@id="fundTyp_input_0"]/option[2]').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
driver.find_element_by_xpath('//*[@id="brcGb_input_3"]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40) # 조건에 맞게 검색되는 시간 30초

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")# 다운받은 파일명 변경작업
file_newname_newfile = os.path.join(file_path, "연금저축국내주식.xls")
os.rename(file_oldname, file_newname_newfile)

#주식 해외 연금저축
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[3]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "연금저축해외주식.xls")
os.rename(file_oldname, file_newname_newfile)

#채권 해외 연금저축
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td[1]/div/div/select/option[5]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "연금저축해외채권.xls")
os.rename(file_oldname, file_newname_newfile)


#채권 국내 연금저축
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(30)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "연금저축국내채권.xls")
os.rename(file_oldname, file_newname_newfile)


#채권 국내 퇴직연금
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[6]/td/ul/li[5]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "퇴직연금국내채권.xls")
os.rename(file_oldname, file_newname_newfile)


#채권 해외 퇴직연금
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[3]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "퇴직연금해외채권.xls")
os.rename(file_oldname, file_newname_newfile)


#주식 해외 퇴직연금
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td[1]/div/div/select/option[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "퇴직연금해외주식.xls")
os.rename(file_oldname, file_newname_newfile)


#주식 국내 퇴직연금
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
time.sleep(40)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(3)

file_oldname = os.path.join(file_path, f"연금상품상세수익률_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "퇴직연금국내주식.xls")
os.rename(file_oldname, file_newname_newfile)


driver.quit()


# In[16]:


#통합 위험등급 데이터 수집

from selenium import webdriver
import time
import os
from datetime import datetime
import pyexcel as px

current_time = datetime.now()
Year = str(current_time.year)
Month = str(current_time.month)
if len(Month)==1:
    Month=str(0)+Month
Day = str(current_time.day)
if len(Day)==1:
    Day=str(0)+Day
Today=Year+Month+Day #오늘날짜를 8자리 숫자로 표현, 다운받을시 파일명에 포함됨

def DeleteAllFiles(filePath): # 파일이 저장될 디렉토리에 기존 파일이 존재한다면 삭제해주는 함수
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

file_path = './static/통합'
DeleteAllFiles(file_path) # 1번셀 자료도 지우므로 사용에 유의

options = webdriver.ChromeOptions()

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
options.add_argument('user-agent=' + user_agent)

options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.

options.add_experimental_option("prefs", {'download.default_directory':r'C:\Users\pc\OneDrive\바탕 화면\Django\mysite\static\통합'})#파일저장 경로 설정

chromedriver = './static/chromedriver.exe'
driver = webdriver.Chrome(chromedriver, options=options)

#통합.xls 만들기/ 통합파일은 분기별 갱신
driver.get('https://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISFundSalRtn.xml&divisionId=MDIS01013004000000&serviceId=SDIS01013004000')
time.sleep(10)

# KB증권 /1.선택탭 클릭, 2.증권사선택, 3.검색
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[21]').click()#이것만 수정
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()# 다운로드
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "KB증권.xls")
os.rename(file_oldname, file_newname_newfile)

#KEB하나은행
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "KEB하나은행.xls")
os.rename(file_oldname, file_newname_newfile)

#NH투자증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[22]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "NH투자증권.xls")
os.rename(file_oldname, file_newname_newfile)

#대신증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[26]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "대신증권.xls")
os.rename(file_oldname, file_newname_newfile)

#미래에셋증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[29]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "미래에셋증권.xls")
os.rename(file_oldname, file_newname_newfile)

#삼성증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[32]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "삼성증권.xls")
os.rename(file_oldname, file_newname_newfile)

#신영증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[34]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "신영증권.xls")
os.rename(file_oldname, file_newname_newfile)

#신한금융투자
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[35]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "신한금융투자.xls")
os.rename(file_oldname, file_newname_newfile)

#신한은행
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[12]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "신한은행.xls")
os.rename(file_oldname, file_newname_newfile)

#유안타증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[36]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "유안타증권.xls")
os.rename(file_oldname, file_newname_newfile)

#키움증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[43]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "키움증권.xls")
os.rename(file_oldname, file_newname_newfile)

#하나금융투자
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[44]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "하나금융투자.xls")
os.rename(file_oldname, file_newname_newfile)

#하이투자증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[45]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "하이투자증권.xls")
os.rename(file_oldname, file_newname_newfile)

#한국투자증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[46]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "한국투자증권.xls")
os.rename(file_oldname, file_newname_newfile)

#한국포스증권
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[47]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
time.sleep(15)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
time.sleep(8)

file_oldname = os.path.join(file_path, f"펀드판매회사 펀드 수익률 공시_{Today}.xls")
file_newname_newfile = os.path.join(file_path, "한국포스증권.xls")
os.rename(file_oldname, file_newname_newfile)

driver.quit()

#통합.xls로 파일처리하기/ 디렉토리 내부의 모든 xls파일 통합하는 방식, 활용에 융의할 필요 있음

print("Process start")
start_time = time.time()

## 폴더명 지정
directory = f"{file_path}"

## 결과 파일명 지정
outfile_name = f"{file_path}/통합.xls"

input_files=os.listdir(directory)

CONTENTS = []

for filename in input_files:
    if ".xls" not in filename:
        continue

    data_array=px.get_array(file_name=directory + "/" + filename)

    header = data_array[0]
    data_array = data_array[1:]

    if len(CONTENTS) == 0:
        CONTENTS.append(header)

    CONTENTS += data_array

    px.save_as(array=CONTENTS, dest_file_name=outfile_name)

print("process done")

end_time = time.time()

print("the job took " + str(end_time - start_time) + "seconds.")


#데이터 통합과정

import pandas as pd

data8 = pd.read_excel('./static/8분류/연금저축국내주식.xls')
name8 = []

for i in range(len(data8)):
    name8.append(data8['펀드명'][i])

name8=name8[1:]

result8 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name8:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result8.append(data9['위험등급'][index])
    else:
        result8.append('NA')

data8['위험등급']=result8
data8.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data8=data8[1:]
data8.to_excel('./static/funds8.xlsx', index=False)


data7 = pd.read_excel('./static/8분류/연금저축국내채권.xls')
name7 = []

for i in range(len(data7)):
    name7.append(data7['펀드명'][i])

name7=name7[1:]

result7 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name7:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result7.append(data9['위험등급'][index])
    else:
        result7.append('NA')

data7['위험등급']=result7
data7.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data7=data7[1:]
data7.to_excel('./static/funds7.xlsx', index=False)


data6 = pd.read_excel('./static/8분류/연금저축해외주식.xls')
name6 = []

for i in range(len(data6)):
    name6.append(data6['펀드명'][i])

name6=name6[1:]

result6 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name6:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result6.append(data9['위험등급'][index])
    else:
        result6.append('NA')

data6['위험등급']=result6
data6.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data6=data6[1:]
data6.to_excel('./static/funds6.xlsx', index=False)


data5 = pd.read_excel('./static/8분류/연금저축해외채권.xls')
name5 = []

for i in range(len(data5)):
    name5.append(data5['펀드명'][i])

name5=name5[1:]

result5 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name5:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result5.append(data9['위험등급'][index])
    else:
        result5.append('NA')

data5['위험등급']=result5
data5.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data5=data5[1:]
data5.to_excel('./static/funds5.xlsx', index=False)

###############################

data4 = pd.read_excel('./static/8분류/퇴직연금국내주식.xls')
name4 = []

for i in range(len(data4)):
    name4.append(data4['펀드명'][i])

name4=name4[1:]

result4 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name4:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result4.append(data9['위험등급'][index])
    else:
        result4.append('NA')

data4['위험등급']=result4
data4.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data4=data4[1:]
data4.to_excel('./static/funds4.xlsx', index=False)


data3 = pd.read_excel('./static/8분류/퇴직연금국내채권.xls')
name3 = []

for i in range(len(data3)):
    name3.append(data3['펀드명'][i])

name3=name3[1:]

result3 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name3:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result3.append(data9['위험등급'][index])
    else:
        result3.append('NA')

data3['위험등급']=result3
data3.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data3=data3[1:]
data3.to_excel('./static/funds3.xlsx', index=False)


data2 = pd.read_excel('./static/8분류/퇴직연금해외주식.xls')
name2 = []

for i in range(len(data2)):
    name2.append(data2['펀드명'][i])

name2=name2[1:]

result2 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name2:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result2.append(data9['위험등급'][index])
    else:
        result2.append('NA')

data2['위험등급']=result2
data2.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data2=data2[1:]
data2.to_excel('./static/funds2.xlsx', index=False)


data1 = pd.read_excel('./static/8분류/퇴직연금해외채권.xls')
name1 = []

for i in range(len(data1)):
    name1.append(data1['펀드명'][i])

name1=name1[1:]

result1 = ['위험등급']
data9 = pd.read_excel('./static/통합/통합.xls')

for name in name1:
    if name in list(data9['펀드명']):
        index=data9[data9['펀드명'] == name].index[0]
        result1.append(data9['위험등급'][index])
    else:
        result1.append('NA')

data1['위험등급']=result1
data1.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
data1=data1[1:]
data1.to_excel('./static/funds1.xlsx', index=False)



