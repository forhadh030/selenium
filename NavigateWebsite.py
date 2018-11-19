#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""A really good docstring"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# The website
driver = webdriver.Firefox()
driver.get("http://magento-demo.lexiconn.com")

# Men section of the webpage
men = driver.find_element_by_xpath("/html/body/div/div[2]/header/div/div[3]/nav/ol/li[2]")
men.click()

# Denim section
denim = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/ul/li[4]/a/img")
denim.click()
detail = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/div/div[2]/a")
detail.click()

# Selecting the color of the Denim
color = Select(driver.find_element_by_id("attribute92"))
color.select_by_visible_text("Indigo")

# Selecting the size of the Denim
size = Select(driver.find_element_by_id("attribute180"))
size.select_by_visible_text("32")

# Add to Cart
submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/form/div[3]/div[6]/div[2]/div[2]/button")
submit.click()

# Proceed to checkout
checkout = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li/button")
checkout.click()