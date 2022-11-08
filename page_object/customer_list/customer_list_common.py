# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 17:08
# @Author  : LCQ
# @FileName: customer_list_common.py


from common.base_operate import BaseOperate
from page_object.customer_list.customer_list_locator import CustomerListLocator

class CustomerListCommon(BaseOperate,CustomerListLocator):

    # 勾选客户
    def check_customner(self,num=1):
        for i in range(num):
            self.clickElement(self.customer_list_checkbox, index=i,scroll=0)