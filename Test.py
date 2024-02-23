from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "14",
    "deviceName": "Pixel device",
    "app": "/Users/mac/Downloads/theScore.apk",
    "udid": "emulator-5554",
    "appPackage": "com.fivemobile.thescore",
}
appium_server_url = 'http://0.0.0.0:4723/wd/hub'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)


# Define wait timeout
wait_timeout = 30

# Explicit wait
get_started_button = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/btn_primary'))
)
assert get_started_button.is_displayed(), "Element is not visible.Page is not as expected"
get_started_button.click()

# Explicit wait for the 'NBA Basketball' element
element = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.fivemobile.thescore:id/txt_name" and @text="NBA Basketball"]'))
)
assert element.is_displayed(), "Element is not visible.Page is not as expected"
element.click()

# Explicit wait for the second continue button
continue_button1 = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/btn_primary'))
)
assert continue_button1.is_displayed(), "Element is not visible.Page is not as expected"
continue_button1.click()

# Explicit wait for the allow button
allow_btn = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/btn_allow'))
)
assert allow_btn.is_displayed(), "Element is not visible.Page is not as expected"
allow_btn.click()

# Explicit wait for the allow while using app button
allow_while_using_app = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'))
)
assert allow_while_using_app.is_displayed(), "Element is not visible.Page is not as expected"

allow_while_using_app.click()

# Explicit wait for the favorite team element
favourite_team = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.fivemobile.thescore:id/recyclerView"]/android.widget.LinearLayout[1]'))
)
assert favourite_team.is_displayed(), "Element is not visible.Page is not as expected"
favourite_team.click()

# Explicit wait for the continue button
continue_button2 = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/btn_primary'))
)
# Assertions
assert continue_button2.is_displayed(), "Element is not visible.Page is not as expected"

continue_button2.click()

# Explicit wait for the Done button
Done_Button = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/btn_primary'))
)
assert Done_Button.is_displayed(), "Element is not visible.Page is not as expected"

Done_Button.click()

# Explicit wait for the allow notification button
allow_notification = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.android.permissioncontroller:id/permission_allow_button'))
)
assert allow_notification.is_displayed(), "Element is not visible.Page is not as expected"
allow_notification.click()

team_search_field = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/search_bar_text_view'))
)
assert team_search_field.is_displayed(), "Element is not visible.Page is not as expected"
team_search_field.click()

team_search_field2 = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.ID, 'com.fivemobile.thescore:id/search_src_text'))
)
assert team_search_field2.is_displayed(), "Element is not visible.Page is not as expected"
team_search_field2.click()
team_search_field2.send_keys('Toronto Raptors')

# implicit wait is used to get the data from the search query
driver.implicitly_wait(30)


allow_notification = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.fivemobile.thescore:id/recyclerView"]/android.widget.LinearLayout[1]'))
)
assert allow_notification.is_displayed(), "Element is not visible.Page is not as expected"

allow_notification.click()


player_stats = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.LinearLayout[@content-desc="Player Stats"]'))
)
assert player_stats.is_displayed(), "Element is not visible.Players stats are not displayed"
player_stats.click()

Barne_player_name = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.fivemobile.thescore:id/txt_name" and @text="S. Barnes"]'))
)
assert Barne_player_name.is_displayed(), "S. Barne Player is not displayed"

Trent_player_name = WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.fivemobile.thescore:id/txt_name" and @text="G. Trent"]'))
)
assert Trent_player_name.is_displayed(), "Trent Player is not displayed"

# Go back to the previous screen
driver.back()

#All heading should be there to show all teams below as list
previous_page_assertion1 =  WebDriverWait(driver, wait_timeout).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.LinearLayout[@content-desc="All"]'))
)
assert previous_page_assertion1.is_displayed(), " All section is not displayed"







