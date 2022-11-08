# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 10:12
# @Author  : LCQ
# @FileName: init_driver.py

import os,sys,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.operate_file import OperateFile

def init_driver(browser='chrome'):
    # 加启动配置
    try:
        project_dir=os.path.dirname(os.path.dirname(__file__))
        download_path=os.path.join(project_dir,'download')
        driver_path=os.path.join(project_dir,'driver')
        system = sys.platform
        if browser=='chrome':
            options = webdriver.ChromeOptions()
            if 'win' in system:
                driverPath = os.path.join(driver_path,'chromedriver.exe')
            elif 'linux' in system:
                driverPath = '/usr/bin/chromedriver'
            else:
                assert False, '其他运行环境需要进行配置！'
        elif browser=='ie':
            options = webdriver.IeOptions()
            if 'win' in system:
                driverPath = os.path.join(driver_path,'IEDriverServer.exe')
            elif 'linux' in system:
                driverPath = '/usr/bin/IEDriverServer'
            else:
                assert False, '其他运行环境需要进行配置！'
        elif browser=='firefox':
            options = webdriver.FirefoxOptions()
            if 'win' in system:
                driverPath = os.path.join(driver_path,'geckodriver.exe')
            elif 'linux' in system:
                driverPath = '/usr/bin/geckodriver'
            else:
                assert False, '其他运行环境需要进行配置！'
        elif browser=='edge':
            options = webdriver.EdgeOptions()
            if 'win' in system:
                driverPath = os.path.join(driver_path,'msedgedriver.exe')
            elif 'linux' in system:
                driverPath = '/usr/bin/msedgedriver'
            else:
                assert False, '其他运行环境需要进行配置！'
        else:
            assert False,'输入的浏览器不存在，请检查！'
        options.add_argument('disable-infobars')
        options.add_argument('--lang=zh-CN')
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1920x1080')
        prefs ={"download.default_directory": download_path,
                "profile.default_content_setting_values.automatic_downloads": 1,
                "download.prompt_for_download": False,
                "directory_upgrade": True,
                "safebrowsing.enabled": True,
                "profile.default_content_setting_values": {"notifications": 2}
        }
        options.add_experimental_option('prefs',prefs)
        driver=webdriver.Chrome(driverPath,options=options)
        driver.maximize_window()
        operate=OperateFile()
        file_path=os.path.join(project_dir,'config','login_data.yaml')
        login_data=operate.read_yaml(file_path)
        driver.get(login_data['login_url'])
        driver.find_element(By.ID,"loginID").send_keys(login_data['username'])
        driver.find_element(By.ID,"loginPassword").send_keys(login_data['password'])
        driver.find_element(By.ID,"loginBtn").click()
        time.sleep(30)
        try:
            # 关闭活动窗
            try:
                driver.execute_script('document.getElementById("closeLink").click()')
            except Exception as Error:
                print(Error)
            driver.execute_script('document.getElementById("activitiesSeasonBtnOne").click()')
            driver.execute_script('document.getElementById("activitiesSeasonBtnTwo").click()')
        except Exception as Error:
            print("没有查找到活动模态框元素：{}".format(Error))
    except Exception as Error:
        assert False,'实例化浏览器失败，错误信息为：%s'%Error
    else:
        return driver