# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 17:03
# @Author  : LCQ
# @FileName: test_customer_list.py

import pytest,allure
from page_object.customer_list.customer_list_page import CustomerListPage

@allure.feature('客户列表')
class TestCustomerList():

    @allure.story('客户列表：批量变更')
    def test_batch_change(self,login):
        self.customerListPage=CustomerListPage(login)
        self.customerListPage.batch_change()

if __name__ == '__main__':
    pytest.main(['test_customer_list.py'])