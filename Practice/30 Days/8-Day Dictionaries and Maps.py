# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:16:45 2019

@author: uppup
"""

items = int(input())
phone_book = {}

for i in range(0, items):
    contact = input().split(' ')
    if not contact[0] in phone_book:
        phone_book.update({contact[0]: contact[1]})

for i in range(0, items):
    contact_name = input()
    if contact_name in phone_book:
        print(contact_name + "=" + phone_book[contact_name])
    else:
        print("Not found")
