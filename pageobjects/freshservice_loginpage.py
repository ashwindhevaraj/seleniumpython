from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage
import time

class freshservice_loginpage(basepage):
    username_field=(By.CSS_SELECTOR,"[id='username']")
    password_field=(By.CSS_SELECTOR,"[id='password']")
    signin_button=(By.CSS_SELECTOR,"[data-testid='login-button']")
    logout_icon=(By.CSS_SELECTOR,"a[id='header-profile-avatar']")
    logout_button=(By.CSS_SELECTOR,"[id='signout-link']")
    ticket_link_button=(By.CSS_SELECTOR,"[title='Tickets']")
    create_new_button=(By.CSS_SELECTOR,"svg#add-new-icon")
    ticket_exact_link=(By.CSS_SELECTOR,"a[title='Ticket']")
    requestor_field=(By.XPATH,"//form[@id='new-ticket-form']//div[@formserv-field-name='requesterId']//div//div//input")
    requestor_exactmatch=(By.XPATH,"//ul[@aria-label='Requester']//li")
    subject_field=(By.CSS_SELECTOR,"input[labeltext='Subject']")
    description_field=(By.XPATH,"//div[@class='fr-wrapper show-placeholder']//div//div")
    ticket_submitbutton=(By.CSS_SELECTOR,"button[id='form-submit']")

    

    def __init__(self,driver):
        super().__init__(driver)

    def login_freshservice(self):
        self.input_text(self.username_field,"aswin.devaraj@freshworks.com")
        self.input_text(self.password_field,"12345678")
        self.click_element(self.signin_button)

    def logout_freshservice(self):
        self.click_element(self.logout_icon)
        self.click_element(self.logout_button)

    def click_tickets_link(self):
        self.click_element(self.ticket_link_button)
        self.click_element(self.create_new_button)
        self.click_element(self.ticket_exact_link)

    def add_ticket_details(self):
        self.click_element(self.requestor_field)
        self.input_text(self.requestor_field,"aswin.devaraj@freshworks.com")
        self.click_element(self.requestor_exactmatch)
        self.click_element(self.subject_field)
        self.input_text(self.subject_field,"Automationtext1")
        self.scroll_to_an_element(self.description_field)
        self.click_element(self.description_field)
        time.sleep(5)
        self.input_text(self.description_field,"Automation added this da")
        self.click_element(self.ticket_submitbutton)




    




    
