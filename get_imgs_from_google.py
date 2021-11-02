"""
Get and save images from Google images,
original code at
https://dev.to/ericchapman/python-get-and-save-google-images-with-selenium-42i1
"""

from selenium import webdriver
import time, requests


def search_google(search_query, number_of_imgs):
    browser = webdriver.Chrome()
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')

    count = 0
    for elem in elements:
        # get images source url
        elem.click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        response = requests.get(images_url[count])
        if response.status_code == 200:
            with open(f"search{count+1}.jpg", "wb") as file:
                file.write(response.content)

        count += 1

        # Stop get and save after number_of_imgs
        if count == number_of_imgs:
            break

    return images_url

items = search_google('turtles', 5)