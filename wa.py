from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,time
########## ANIMATIONS (Can be commented) ##########
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("S A M", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("WHATSAPP   SPAMMER  !", font='small'),
            int(screen.height / 2 + 3)),
        Cycle(
            screen,
            FigletText("PRESS   '  Q  '   TO STOP!", font='small'),
            int(screen.height/8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])
Screen.wrapper(demo)
############################################################



print('\n\nCLOSE ANY OTHER INSTANCES OF WHATSAPP WEB \n\n')
'''
spam_victim="Script Test"
spam_message_count=1
spam_message=["TEST"]
spam_count=1000
'''
# Get spam details
spam_victim = input('Enter the victim\'s name (exact) in your contact list: ')
spam_message_count = int(input('How many messages do you wanna send? '))
spam_message = []
for i in range(0, spam_message_count):
    spam_message.append(input('Enter the spam message: '))
spam_count = int(input('How many times do you want to spam? '))

print('\n\nSCAN THE QR ON YOUR PHONE. \tTimeout : 30 secs\n\n')
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
try:
    search_box = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.XPATH, '// *[@id="side"]/div[1]/div/label/input'))
    )
    search_box.clear()
    search_box.send_keys(spam_victim)
    search_box.send_keys(Keys.RETURN)
except:
    print("Can't locate search box element!")

try:
    for temp in driver.find_elements_by_css_selector('div._3u328.copyable-text.selectable-text'):
        if temp.get_attribute('contenteditable') == "true":
            msg_box = temp
except:
    print("Can't locate message box element!")

try:    
    for num in range(0, spam_count):
        for message in spam_message:
            msg_box.clear()
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.RETURN)
            # sys.stdout.write("[%-20s] %d%%" % ('='*(num+1), 5*(num+1)))
            # sys.stdout.flush()
            print('\tDONE: ', num+1," / ",spam_count, end='\r', flush=True)
            time.sleep(0.3)

    print('\n\nSPAMMING SUCCESSFUL! EXITING in 10 secs! \n\n')
    time.sleep(10)
    driver.quit()
except:
    print("Can't locate fullname element!")


''' CODE TO GET FIRST NAME OF THE CONTACT
    fullname = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[2]/div[1]/div/span').text
    firstname = fullname.split()
    print(fullname)
    print(firstname)
    msg_box.send_keys("SCRIPT WORKS!" + "\nUser Name = " + firstname[0])
    msg_box.send_keys(Keys.RETURN)
    '''
