# functional_tests/test_recipes.py
import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase, Client
from django.contrib.auth.models import User
from countries.models import Continent, Country
from recipes.models import Recipe
# from notifications.models import Notification, NotificationCategory

class RecipesTest(LiveServerTestCase):
    def setUp(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(5)
        self.username = 'testuser'
        self.password = 'testpassword'
        self.continent = Continent.objects.create(name='test_continent')
        self.country_1 = Country.objects.create(name='test country 1', continent = self.continent)
        self.country_2 = Country.objects.create(name='test country 2', continent = self.continent)
        

    def tearDown(self):
        self.browser.quit()
        # pass

    def login(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.browser.get('%s%s' % (self.live_server_url, '/login/'))
        self.browser.switch_to.active_element.get_attribute("title")
        username_field = self.browser.find_element(by=By.NAME, value='username')
        password_field = self.browser.find_element(by=By.NAME, value='password')
        login_button = self.browser.find_element(by=By.ID, value='login')
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()


    '''def test_countries_are_shown_in_list(self):
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
        self.browser.quit()'''

    '''def test_recipes_are_saved(self):
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

        username_field.send_keys('test')
        password_field.send_keys('testpassword')
        login_button.click()

        # John should be redirected to the homepage
        explore_button = self.browser.find_element(by=By.ID, value='explore')
        self.assertEqual(explore_button.text, 'Explore')
        
        # John navigates back to the original recipe that he wanted to save -> can skip straight to it
        # as the navigation to a recipe has already been tested
        self.browser.get('%s%s' % (self.live_server_url, '/recipes/1/test-recipe-1/'))
        self.browser.switch_to.active_element.get_attribute("title")
        
        save_button = self.browser.find_element(by=By.NAME, value='recipe_save')
        self.assertEqual(save_button.text, 'Save Recipe')
        save_button.click()
        save_button = self.browser.find_element(by=By.NAME, value='recipe_save')
        self.assertEqual(save_button.text, 'Recipe Saved')
        # John clicks the save button -> the button text should update to indicate that it is now saved

        # John goes to his dashboard/saved_recipes and sees that the recipe he just saved is now on the list.
        
        dashboard_button = self.browser.find_element(By.ID, 'dashboard')
        self.assertEqual(dashboard_button.text, 'Dashboard')
        dashboard_button.click()

        saved_recipes_button = self.browser.find_element(By.ID, 'saved_recipes')
        self.assertEqual(saved_recipes_button.text, 'Saved Recipes')
        saved_recipes_button.click()'''
        
    def test_recipes_are_made(self):
        self.recipe_1 = Recipe.objects.create(name='test recipe 1', country = self.country_1)
        # John goes to a recipe, and clicks the "I Made It" button.
        self.login()
        self.browser.get('%s%s' % (self.live_server_url, '/recipes/1/test-recipe-1/'))
        self.browser.switch_to.active_element.get_attribute("title")
        made_button = self.browser.find_element(By.NAME, 'recipe_made')
        self.assertEqual(made_button.text, 'I Made It!')
        

        # Upon clicking this, the logic should update to see if any badges are awarded
        # John should get a badge for completing his first recipe
        # Before clicking, check to see that there are no notifications. Should be blank and not show 0
        num_notifications = self.browser.find_element(By.ID, 'num_notifications')
        self.assertEqual(num_notifications.text, '')
        made_button.click()

        made_button = self.browser.find_element(By.NAME, 'recipe_made')
        self.assertEqual(made_button.text, 'Remove From Made Recipes')

        # John should receive a notification that he got a new badge, and be able to go to the page with all of the badges
        num_notifications = self.browser.find_element(By.ID, 'num_notifications')
        self.assertEqual(int(num_notifications.text), 1)

        # Should be an icon, so can't check for internal text
        notifications_button = self.browser.find_element(By.ID, 'notifications')
        notifications_button.click()

        # Redirected to a page with all of the notifications. Should show all past notifications
        # Notifications should be in two colors based off of read status
        # Option to mark all read, or go to appropriate locations such as badges, recipes, etc.
        new_notification_button = self.browser.find_element(By.XPATH, '//div[@class="notification"]/a')
        self.assertEqual(new_notification_button.text, 'New Badge Awarded')
        # Add details underneath which say which badge was awarded
        new_notification_button.click()
        
        badges = self.browser.find_element(By.ID, 'badges')
        self.assertEqual(badges.text, 'Badges')

    '''def test_notifications_clear(self):
        # Create a notification to test with
        self.badge_category = NotificationCategory.objects.create(name='Badge Awarded')
        self.notification = Notification.objects.create(category=self.badge_category, description='You earned a badge for making your first recipe', read=False)
        # John should be able to clear the notification saying that he earned a new badge. Must navigate back to the notifications page
        notifications_button = self.browser.find_element(By.ID, 'notifications')
        notifications_button.click()

        unread_notifications = self.browser.find_element(By.XPATH, '//div[@class="notification unread"]/h3')
        self.assertEqual(unread_notifications.text, 'Badge Awarded')
        # Check that mark all read works
        mark_all_read_button = self.browser.find_element(By.ID, 'mark_all_read')
        self.assertEqual(mark_all_read_button.text, 'Mark all read')

        read_notifications = self.browser.find_element(By.XPATH, '//div[@class="notification read"]/h3')
        self.assertEqual(read_notifications.text, 'Badge Awarded')

        # Reset and check that individual 
        self.notification.read = False

        unread_notifications = self.browser.find_element(By.XPATH, '//div[@class="notification unread"]/h3')
        self.assertEqual(unread_notifications.text, 'Badge Awarded')
        # Check that mark read works
        mark_read_button = self.browser.find_element(By.NAME, 'mark_read')
        self.assertEqual(mark_read_button.text, 'Read')
        mark_all_read_button.click()

        read_notifications = self.browser.find_element(By.XPATH, '//div[@class="notification read"]/h3')
        self.assertEqual(read_notifications.text, 'Badge Awarded')'''






    '''def test_reviews_are_posted(self):
        pass
        # John finds a recipe he likes and wants to leave a review of it
        # John wants to leave a rating out of 5 stars, as well as a text comment about it
        # John should be able to edit his review after he makes it.
        # John should see the number of reviews increase after he leaves his review as well as seeing the average of the ratings
        # John should get another badge for leaving his first review, and get a notification that he earned a new badge
    '''


        



        