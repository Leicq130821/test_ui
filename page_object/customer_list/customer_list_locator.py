# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 16:55
# @Author  : LCQ
# @FileName: customer_list_locator.py


class CustomerListLocator():

    # 合并至客户input
    merge_to_customer_input='//label[text()="合并至"]/following-sibling::span//input'
    # 写信页面邮件地址
    writeEmailPageEmailAddress='//div[@class="address_list"]//p[contains(@class,"show_txt")]'
    # 客户列表复选框
    customer_list_checkbox='//div[@class="ft_table_body"]//span[contains(@class,"el-checkbox__input")]'
    # 邮件主题输入框
    emailSubjectInput='//input[@id="subjectName"]'
    # 邮件发送按钮
    emailSendButton='//button[contains(@class,"send")]'
    # 发送邮件下拉箭头
    sendEmailDownArrow='//span[text()="发送邮件"]/parent::*/following-sibling::div//i[@class="el-icon-arrow-down"]'
    # 颜色代码输入框
    colorCodeInput='//span[@class="el-color-dropdown__value"]//input'