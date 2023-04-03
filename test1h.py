site = "http://naver.com"

#1. http:// 제외
site = site.replace("http://","")

site = site[:site.index(".")]
pw = site

length = str(len(site))
pw = site[:3] + str(len(site))
pw += str(site.count("e"))
pw += "!"

print("{0}의 비밀번호는 {1} 입니다." .format(site, pw))

