from DrissionPage import ChromiumPage
from DrissionPage.common import Actions
from DrissionPage.common import Keys
import os



# 平台账号密码
usernmae = ''
password = ''

# 根据平台项目顺序进行添加
categorys = [
    'category1',
    'category2',
    'category3',
]

# projectName : 平台爬虫名称
# spiderName : 爬虫名称（用于命令启动）
# category : 平台项目分类 （在上面categorys顺序进行选择序号, 1 -> category1）
spiderInfos = [
    {'projectName': '测试1', 'spiderName': 'test1', 'category': 1}, 
    {'projectName': '测试2', 'spiderName': 'test2', 'category': 2}, 
    ]









# 当前文件所在的目录
curDirPath = os.path.dirname(__file__)

# # 打开浏览器
adminUrl = 'http://crawlab.ztesa.site/#/login'
page = ChromiumPage()
page.get(adminUrl)
page.wait.ele_displayed('@name=username')

# 登录管理平台
if page.ele("xpath://button[@class='el-button el-button--primary el-button--large']"):
    page.ele('@name=username').input(usernmae)
    page.ele('@name=password').input(password)
    page.ele("xpath://button[@class='el-button el-button--primary el-button--large']").click()


for spiderInfo in spiderInfos:

    projectName = spiderInfo['projectName']
    command = 'scrapy crawl {}'.format(spiderInfo['spiderName'])
    category = spiderInfo['category']
    spiderPath = os.path.join(curDirPath, spiderInfo['spiderName'])


    # 创建爬虫
    page.wait.ele_displayed("xpath://span[@class='menu-item-title' and contains(text(), '爬虫')]")
    page.ele("xpath://span[@class='menu-item-title' and contains(text(), '爬虫')]").click()
    page.ele("xpath://button[contains(@title, '添加一个新爬虫')]").click()
    page.ele("xpath://input[@id='name']").input(projectName)
    page.ele("xpath://input[@id='cmd']").input(command)
    ac = Actions(page)
    ac.move_to("xpath://input[@id='project']").click()
    for i in range(category):
        ac.key_down(Keys.DOWN)
    ac.key_down(Keys.ENTER)
    page.ele("xpath: //*[@class='el-dialog create-edit-dialog visible']//span[@id='confirm-btn']").click()


    # 上传爬虫文件
    page.ele("xpath://span[@class='menu-item-title' and contains(text(), '爬虫')]").click()
    page.ele("xpath: //tr[@class='el-table__row'][1]//button[@title='查看']").click()
    page.ele("xpath: //li[@class='el-menu-item files']").click()
    page.ele("xpath: //button[@title='上传文件']").click()

    page.set.upload_files(spiderPath)
    page.ele("xpath: //button[@class='el-button el-button--primary el-button--large']").click()
    page.wait.upload_paths_inputted()

    page.ele("xpath: /html//div[1]/section/section/div[3]/div[2]/div/div/div[3]/span[2]/button").click()
    print(projectName, '-- 上传成功')
    page.wait(2)