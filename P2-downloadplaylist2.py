import os, urllib.request, re
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

#apt-get install xvfb

def start(save, playlistName, type):

    driver = webdriver.Chrome('C:/Users/Rishita/Documents/Intellify python./chromedriver')
    driver.get('http://en.savefrom.net/')

    inputtext = driver.find_element_by_id('sf_url')
    inputtext.send_keys(save)

    enter = driver.find_element_by_id('sf_submit')
    enter.submit()

    sleep(20)

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    page = BeautifulSoup(html, "html.parser")
    div = page.find_all('div', class_='def-btn-box')
    for download in div:
        link = download.findAll('a')[0].get('href')
        name = download.findAll('a')[0].get('download')
        print ("Downloading:", name)
        cmd = 'wget --progress=bar:force -Ncq -e "convert-links=off" --keep-session-cookies --save-cookies /dev/null --no-check-certificate "%s" -O %s --show-progress' % (
            link, re.escape(name))
        if type == 1:
            os.system('cd %s;%s' % (re.escape(playlistName), cmd))
        else:
            os.system(cmd)

    driver.quit()

def download(downloadUrl, value):

    if value == 1:
        driver = webdriver.Chrome('C:/Users/Rishita/Documents/Intellify python./chromedriver')
        driver.get(downloadUrl)

        response = driver.find_element_by_id('pl-video-list')
        try:
            load = response.find_element_by_xpath('//button[contains(@aria-label,"Load more")]')
            sleep(5)
            load.click()
        except NoSuchElementException:
            ""
        sleep(10)

        playlist = driver.execute_script("return document.getElementsByTagName('body')[0].innerHTML")
        driver.quit()
        content = BeautifulSoup(playlist, "html.parser")
        title = content.find_all('td', class_='pl-video-title')
        playlistName = content.find('h1', class_='pl-header-title').text.strip()
        if not os.path.exists(playlistName):
            os.mkdir(playlistName)
            print ('Created Directory With Playlist Name:', playlistName)

        for href in title:
            url = href.find('a').get('href')
            save = 'https://www.youtube.com%s' % url
            start(save, playlistName, 1)

    if value == 2:
        start(downloadUrl,'', 2)

def switch(choice):
    if choice == '1':
        playlistUrl = input('Enter Url Of Youtube Playlist: ')
        download(playlistUrl, 1)

    elif choice == '2':
        videoUrl = input('Enter Url Of Youtube Video: ')
        download(videoUrl, 2)

    else:
        print ('Please Press 1 or 2.')
        exit(1)

def banner():
    print ('\n')
    print ('\t\t\t###################################################################################################################')
    print ('\t\t\t##         *     *                                             *   *                                             ##')
    print ('\t\t\t##          *   *                                              *   *                                             ##')
    print ('\t\t\t##           * *  **   *   *  ***  *   *  * *   * * *          *   * ***  * *   * * *   **                       ##')
    print ('\t\t\t##            *  *  *  *   *   *   *   *  *  *  *              *   *  *   *  *  *      *  *                      ##')
    print ('\t\t\t##            *  *  *  *   *   *   *   *  * *   * * *          *   *  *   *  *  * * *  *  *                      ##')
    print ('\t\t\t##            *  *  *  *   *   *   *   *  *  *  *              *   *  *   *  *  *      *  *                      ##')
    print ('\t\t\t##            *   **   * * *   *   * * *  * *   * * *            *   ***  * *   * * *   **                       ##')
    print ('\t\t\t##                                                                                                               ##')
    print ('\t\t\t##                             * * *                                                                             ##')
    print ('\t\t\t##                             *     *                                                                           ##')
    print ('\t\t\t##                             *      *   **   *     *  *     *  *       **       *      * *   * * *  * *        ##')
    print ('\t\t\t##                             *      *  *  *  *     *  * *   *  *      *  *     * *     *  *  *      *   *      ##')
    print ('\t\t\t##                             *      *  *  *  *  *  *  *  *  *  *      *  *    *   *    *  *  * * *  * **       ##')
    print ('\t\t\t##                             *     *   *  *  * * * *  *   * *  *      *  *   * *** *   *  *  *      *  *       ##')
    print ('\t\t\t##                             * * *      **   **   **  *     *  * * *   **   *       *  * *   * * *  *    *     ##')
    print ('\t\t\t##                                                                                                               ##')
    print ('\t\t\t##                                                                                                               ##')
    print ('\t\t\t##                                                                                            --knownUnknown     ##')
    print ('\t\t\t###################################################################################################################')


if __name__ == '__main__':

    banner()

    display = Display(visible=0, size=(800, 800))
    display.start()

    print ('\n\n\t\tPress 1 to download Youtube Playlist.\n\t\tPress 2 to download Youtube Video.')
    choice = input('\t>')

    switch(choice)

    display.stop()