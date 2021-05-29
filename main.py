from crawling import crawling_first
from crawling import crawling_second
from viewing import viewing
if __name__ == '__main__':
    path = '' # 填入文件保存路径
    crawling_first()
    crawling_second(path)
    viewing(path)
