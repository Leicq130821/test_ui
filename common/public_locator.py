# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 9:10
# @Author  : LCQ
# @FileName: public_locator.py

class PublicLocator():

    # 切换语言
    switch_language='//div[@data-check="{}"]'
    # 操作成功
    operate_success = '//i[contains(@class,"success")]/following-sibling::p'
    # 根据文本查找div
    text_div='//div[text()="{}"]'
    # 根据id属性查找div
    id_div='//div[@id="{}"]'
    # 根据href属性查找超链接
    href_link='//a[@href="{}"]'
    # 根据text查找span
    text_span='//span[text()="{}"]'
    # 根据包含text查找span
    contains_text_span='//span[contains(text(),"{}")]'
    # 下拉选项
    dropdown_option = '//*[@x-placement]//*[text()="{}"]'
    # 根据包含class属性查找div
    contains_class_div='//div[contains(@class,"{}")]'
    # 根据文本查找label
    text_label='//label[text()="{}"]'
    # 根据占位符查找输入框
    placeholder_input = '//input[@placeholder="{}"]'
    # 根据占位符查找长文本输入框
    placeholder_textarea='//textarea[@placeholder="{}"]'