# functional_tests/test_recipes.py

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

from countries.models import Continent, Country
from recipes.models import Recipe

class RecipesTest(LiveServerTestCase):
    def setUp(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(5)
        self.continent = Continent.objects.create(name='test_continent')
        self.country_1 = Country.objects.create(name='test country 1', continent = self.continent)
        self.country_2 = Country.objects.create(name='test country 2', continent = self.continent)

    def tearDown(self):
        # self.browser.quit()
        pass

    def test_countries_are_shown_in_list(self):
        # John goes to the home page
        self.browser.get(self.live_server_url)

        # He sees a button that says "Explore". He clicks the explore button.
        explore_button = self.browser.find_element(by=By.ID, value='explore')
        self.assertEqual(explore_button.text, 'Explore')
        explore_button.click()

        # The page refreshes and John sees a list of countries, and a search bar with a button that says "Travel"
        self.browser.implicitly_wait(5)
        search_input = self.browser.find_element(by=By.ID, value='search')
        self.assertEqual(search_input.get_attribute('placeholder'), 'Find a destination')

        # John enters a country name and clicks the travel button
        search_input.send_keys('test country 2')
        travel_button = self.browser.find_element(by=By.ID, value='travel')
        self.assertEqual(travel_button.text, 'Travel')
        travel_button.click()
        
        # The page refreshes and John notices the country name is the only country still shown
        # Need to add a query function to ensure that everything
        self.browser.implicitly_wait(5)
        country = self.browser.find_element(by=By.XPATH, value='//div[@class="country"]/h3')
        self.assertEqual(country.text, 'test country 2')
        # country.click()
        self.browser.quit()

    def test_recipes_are_saved(self):
        # Add in code to get to the list of recipes for test_country_1
        # The current test will never work as the test doesn't know which page to start from
        # Add in slug field to make things more readable
        self.recipe_1 = Recipe.objects.create(name='test recipe 1', country = self.country_1)
        self.recipe_2 = Recipe.objects.create(name='test recipe 2', country = self.country_1)
        self.browser.get('%s%s' % (self.live_server_url, '/countries/1/'))
        self.browser.switch_to.active_element.get_attribute("title")
        # The page refreshes and John is now presented with a list of recipes from test_country_1
        recipe = self.browser.find_element(by=By.XPATH, value="//div[@class='recipe-card']/a")
        recipe.click()

        # John selects a recipe and the page reloads to show the details of the recipe
        recipe_title = self.browser.find_element(by=By.ID, value='recipe_title')
        self.assertIsNotNone(recipe_title.text)

        # John wants to save the recipe, but must be logged in to do so
        # He sees text that tells him to log in to save the recipe -> The save_button should not be presented
        login_required = self.browser.find_element(by=By.CLASS_NAME, value='login_required')
        self.assertEqual(login_required.text, 'Login To Save Recipe')

        # John looks on the page, finds the login button and clicks the login button
        login_button = self.browser.find_element(by=By.ID, value='login')
        self.assertEqual(login_button.text, 'Login')
        login_button.click()

        # John doesn't have an account, so he must create a new account
        create_account_button = self.browser.find_element(by=By.ID, value='create_account')
        self.assertEqual(create_account_button.text, 'Create Account')
        create_account_button.click()

        # The page reloads, and John is taken to the login form which asks for a username, email, password, and repeat password
        # He fills out the form and clicks the button to create his account
        username_field = self.browser.find_element(by=By.NAME, value='username')
        email_field = self.browser.find_element(by=By.NAME, value='email')
        password_1_field = self.browser.find_element(by=By.NAME, value='password1')
        password_2_field = self.browser.find_element(by=By.NAME, value='password2')
        submit_button = self.browser.find_element(by=By.ID, value='submit')

        self.assertEqual(username_field.get_attribute('placeholder'), 'Username')
        self.assertEqual(email_field.get_attribute('placeholder'), 'Email')
        self.assertEqual(password_1_field.get_attribute('placeholder'), 'Password')
        self.assertEqual(password_2_field.get_attribute('placeholder'), 'Repeat Password')
        self.assertEqual(submit_button.text, 'Create Account')

        username_field.send_keys('test')
        email_field.send_keys('test@test.com')
        password_1_field.send_keys('testpassword')
        password_2_field.send_keys('testpassword')
        submit_button.click()

        # John is redirected to the login screen where he enters his username and password to login
        username_field = self.browser.find_element(by=By.NAME, value='username')
        password_field = self.browser.find_element(by=By.NAME, value='password')
        login_button = self.browser.find_element(by=By.ID, value='login')

        self.assertEqual(username_field.get_attribute('placeholder'), 'Username')
        self.assertEqual(password_field.get_attribute('placeholder'), 'Password')
        self.assertEqual(login_button.text, 'Login')

        login_button.click()

        # John should be redirected to the homepage

        # John navigates back to the original recipe that he wanted to save -> can skip straight to it
        # as the navigation to a recipe has already been tested

        # save_button = self.browser.find_element(by=By.ID, value='save')
        # self.assertEqual(save_button.text, 'Save Recipe')

        # John clicks the save button -> the button text should update to indicate that it is now saved

        # John goes to his dashboard/saved_recipes and sees that the recipe he just saved is now on the list.
        # There should be options to filter by date added, alphabetical, and even have a search bar to look within saved recipes


        



        