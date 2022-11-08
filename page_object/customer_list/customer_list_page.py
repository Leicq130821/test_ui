# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 16:54
# @Author  : LCQ
# @FileName: customer_list_page.py

import allure,time
from common.base_operate import BaseOperate
from page_object.customer_list.customer_list_locator import CustomerListLocator
from page_object.customer_list.customer_list_common import CustomerListCommon

class CustomerListPage(BaseOperate,CustomerListLocator):

    def __init__(self,driver):
        super().__init__(driver)
        self.clickElement(self.text_div.format('客户'))
        self.customerListCommon=CustomerListCommon(driver)

    # 客户列表：批量变更
    def batch_change(self):
        batchChangeDatas=[{'change':'客户类型','value':'货代'},
                          {'change':'客户等级','value':'一般'},
                          {'change':'客户来源','value':'互联网'},
                          {'change':'业务类型','value':'贸易公司'},
                          {'change':'主营产品','value':'电器'},
                          {'change':'国家/地区','value':'中国大陆'},
                          {'change':'跟进阶段','value':'资料获得'},
                          {'change':'颜色标识','value':'#09A5F4'},
                          {'change':'下一跟进周期','value':time.strftime('%Y-%m-%d')},
                          {'change':'备注','value':'备注'}]
        for batchChangeData in batchChangeDatas:
            with allure.step('勾选两个客户，点击批量变更，选择%s进行变更。'%batchChangeData['change']):
                self.customerListCommon.check_customner(2)
                self.clickElement(self.text_span.format('批量变更'))
                self.clickElement(self.merge_to_customer_input.replace('合并至','选择修改对象'))
                self.clickElement(self.dropdown_option.format(batchChangeData['change']))
                if batchChangeData['change']=='国家/地区':
                    self.elementSendKeys(self.merge_to_customer_input.replace('合并至',batchChangeData['change']),batchChangeData['value'],clear=0)
                    self.clickElement(self.dropdown_option.format(batchChangeData['value']))
                elif batchChangeData['change']=='颜色标识':
                    self.clickElement(self.contains_class_div.format('el-color-picke'))
                    self.elementSendKeys(self.colorCodeInput,batchChangeData['value'])
                    self.clickElement(self.contains_text_span.format('确定'),1)
                elif batchChangeData['change']=='下一跟进周期':
                    self.elementSendKeys(self.placeholder_input.format('请选择时间'),batchChangeData['value'])
                    self.clickElement(self.text_label.format('下次跟进时间'))
                elif batchChangeData['change']=='备注':
                    self.elementSendKeys(self.placeholder_textarea.format('请输入备注'),batchChangeData['value'])
                else:
                    self.clickElement(self.merge_to_customer_input.replace('合并至', batchChangeData['change']))
                    self.clickElement(self.dropdown_option.format(batchChangeData['value']))
                self.clickElement(self.text_span.format('确定'))
                self.sleep(1)
                self.clickElement(self.text_span.format('确定'),1)
                self.findVisibleElement(self.operate_success)
                self.getScreenshot()
                while self.judgeElementExist(self.operate_success,2):
                    self.sleep(1)