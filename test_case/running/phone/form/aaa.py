import json
import requests
import unittest
from requests.auth import HTTPBasicAuth

class JenkinsGettestcase(unittest.TestCase):
    ''''''
    def setUp(self):
        self.r = requests.get('http://192.168.80.199:8081/jenkins/api/json?tree=jobs[name]',auth=('administrator','Teemlink2010'))
        self.build_job_url = 'http://192.168.80.199:8081/jenkins/job/obpm/build'

    def test_get_job_case(self):
        result = self.r.text
        json_result = json.loads(result) #总结：json.dumps : dict转成str  json.loads:str转成dict
        print(json_result)
        self.assertEqual(json_result['jobs'][0]['name'],'obpm')

    def test_build_job_case(self):
        r = requests.post(self.build_job_url,data={},auth=('administrator','Teemlink2010'))
        print(r.status_code)


if __name__ == '__main__':
    unittest.main()

# def GetMiddleStr(content,startStr,endStr):
#     print(str(content.count(startStr))) #获取文本中有多少个def
#     f = open('D:/bnew 2.txt','r',encoding='UTF-8')
#     for line in f.readlines():  # 依次读取每行
#         text = str(line)
#         startIndex = text.find(startStr)#获取开始查找字符的位置
#         #print("位置光标---》》"+str(startIndex))
#         if startIndex==4:
#             endIndex = text.find(endStr) #获取结束查找字符的位置
#             print(text[startIndex:endIndex])
#
# if __name__=='__main__':
#     content = open('D:/bnew 2.txt','r',encoding='UTF-8')
#     content2 = content.read()
#     print(GetMiddleStr(content2, 'def', '(self)'))




