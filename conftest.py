import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.elements.text_box_tab import TextBoxTab
from pages.elements.check_box_tab import CheckBoxTab
from pages.elements.radio_button_tab import RadioButtonTab
from pages.elements.web_tables_tab import WebTablesTab
from pages.elements.buttons_tab import ButtonsTab
from pages.elements.upload_and_download_tab import UploadAndDownloadTab
from pages.elements.links_tab import LinksTab
from pages.elements.broken_links_tab import BrokenLinkTab
from pages.elements.dynamic_properties import DynamicProperties
from pages.forms.practice_form import PracticeFormTab
from pages.alerts_frame_window.browser_window_page import BrowserWindowTab
from pages.alerts_frame_window.modal_dialogs_page import ModalDialogsTab
from pages.alerts_frame_window.alerts_page import AlertsTab
from pages.alerts_frame_window.frames_page import IframePage
from pages.alerts_frame_window.nested_frames_page import NestedIframePage
from pages.widgets.accordian_page import AccordianTab
from pages.widgets.auto_complete_page import AutoCompleteTab
from pages.widgets.date_picker_page import DatePickerTab
from pages.widgets.menu_page import MenuTab
from pages.widgets.progress_bar_page import ProgressBarTab
from pages.widgets.select_menu_page import SelectMenuTab
from pages.widgets.slider_page import SliderTab
from pages.widgets.tabs_page import TabsPageTab
from pages.widgets.tool_tips_page import ToolTipsTab
from pages.book_store.register_and_login_pages import RegisterLoginPage
from pages.book_store.profile_page import ProfilePage
from pages.book_store.book_store_page import BookStorePage
from pages.interactions.sortable_page import SortableTab
from pages.interactions.selectable_page import SelectableTab
from pages.interactions.resizable_page import ResizableTab
from pages.interactions.droppable_page import DroppableTab
from pages.interactions.dragabble_page import DragabbleTab

# chromedriver setups

@pytest.fixture()
def chromedriver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    download_folder_path = {'download.default_directory':
                                'C:\\Users\\sapko\\Desktop\\Project\\PythonUIfwk\\'
                                'Python-UI-Api-test\\files_for_tests\\avatar.jpg'}
#    path_to_adblock = "C:\\Users\\"
#    options.add_argument('load-extension=' + path_to_adblock)
    options.add_experimental_option("prefs", download_folder_path)
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.fixture()
def headed_chromedriver():
    options = Options()
    options.add_argument('--start-maximized')
#    path_to_adblock = "C:\\Users\\ymaka\\Desktop\\4.46.2_0"
#    options.add_argument('load-extension=' + path_to_adblock)
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)

# driver setups

# elements tab


@pytest.fixture()
def text_box(chromedriver):
    return TextBoxTab(chromedriver)


@pytest.fixture()
def check_box(chromedriver):
    return CheckBoxTab(chromedriver)


@pytest.fixture()
def radio_button(chromedriver):
    return RadioButtonTab(chromedriver)


@pytest.fixture()
def web_tables(chromedriver):
    return WebTablesTab(chromedriver)


@pytest.fixture()
def buttons_tab(chromedriver):
    return ButtonsTab(chromedriver)


@pytest.fixture()
def upload_and_download(chromedriver):
    return UploadAndDownloadTab(chromedriver)


@pytest.fixture()
def links_page(chromedriver):
    return LinksTab(chromedriver)


@pytest.fixture()
def browser_windows(chromedriver):
    return BrowserWindowTab(chromedriver)


@pytest.fixture()
def broken_link_tab(chromedriver):
    return BrokenLinkTab(chromedriver)

# practice form tab


@pytest.fixture()
def practice_form(chromedriver):
    return PracticeFormTab(chromedriver)

# alerts, frames and windows page


@pytest.fixture()
def modal_dialogs(chromedriver):
    return ModalDialogsTab(chromedriver)


@pytest.fixture()
def alerts_page_tab(headed_chromedriver):
    return AlertsTab(headed_chromedriver)


@pytest.fixture()
def dynamic_properties(chromedriver):
    return DynamicProperties(chromedriver)


@pytest.fixture()
def iframe_tab(chromedriver):
    return IframePage(chromedriver)


@pytest.fixture()
def nested_iframe_tab(chromedriver):
    return NestedIframePage(chromedriver)

# widgets tab


@pytest.fixture()
def accordian_tab(chromedriver):
    return AccordianTab(chromedriver)


@pytest.fixture()
def auto_complete_tab(chromedriver):
    return AutoCompleteTab(chromedriver)


@pytest.fixture()
def date_picker_tab(headed_chromedriver):
    return DatePickerTab(headed_chromedriver)


@pytest.fixture()
def menu_tab(chromedriver):
    return MenuTab(chromedriver)


@pytest.fixture()
def progress_bar_tab(chromedriver):
    return ProgressBarTab(chromedriver)


@pytest.fixture()
def select_menu_tab(chromedriver):
    return SelectMenuTab(chromedriver)


@pytest.fixture()
def slider_tab(chromedriver):
    return SliderTab(chromedriver)


@pytest.fixture()
def tabs_page(chromedriver):
    return TabsPageTab(chromedriver)


@pytest.fixture()
def tool_tips_tab(chromedriver):
    return ToolTipsTab(chromedriver)

# interactions page


@pytest.fixture()
def sortable_tab(chromedriver):
    return SortableTab(chromedriver)


@pytest.fixture()
def selectable_tab(chromedriver):
    return SelectableTab(chromedriver)


@pytest.fixture()
def resizable_tab(chromedriver):
    return ResizableTab(chromedriver)


@pytest.fixture()
def droppable_tab(headed_chromedriver):
    return DroppableTab(headed_chromedriver)


@pytest.fixture()
def dragabble_tab(chromedriver):
    return DragabbleTab(chromedriver)

# book store


@pytest.fixture()
def login_and_register_tab(headed_chromedriver):
    return RegisterLoginPage(headed_chromedriver)


@pytest.fixture()
def book_store_tab(headed_chromedriver):
    return BookStorePage(headed_chromedriver)


@pytest.fixture()
def profile_tab(headed_chromedriver):
    return ProfilePage(headed_chromedriver)

# setups for testing

# elements tab setups


@pytest.fixture()
def setup_for_text_box(chromedriver, text_box):
    text_box.navigate()
    text_box.input_information_to_form()


@pytest.fixture()
def setup_for_check_box(chromedriver, check_box):
    check_box.click_on_checkboxes()


@pytest.fixture()
def setup_for_radio_button(chromedriver, radio_button):
    radio_button.navigate()


@pytest.fixture()
def setup_for_web_tables(chromedriver, web_tables):
    web_tables.navigate()


@pytest.fixture()
def setup_for_buttons_tab(chromedriver, buttons_tab):
    buttons_tab.navigate()


@pytest.fixture()
def setup_for_upload_and_download_tab(chromedriver, upload_and_download):
    upload_and_download.navigate()


@pytest.fixture()
def setup_for_links_tab(chromedriver, links_page):
    links_page.navigate()


@pytest.fixture()
def setup_for_dynamic_properties(chromedriver, dynamic_properties):
    dynamic_properties.navigate()


@pytest.fixture()
def setup_for_broken_link_tab(chromedriver, broken_link_tab):
    broken_link_tab.navigate()

# practice form setup


@pytest.fixture()
def setup_for_practice_form(chromedriver, practice_form):
    practice_form.navigate()

# alerts, frames and window page setups


@pytest.fixture()
def setup_for_browser_windows(chromedriver, browser_windows):
    browser_windows.navigate()


@pytest.fixture()
def setup_for_modal_dialogs(chromedriver, modal_dialogs):
    modal_dialogs.navigate()


@pytest.fixture()
def setup_for_alerts_tab(headed_chromedriver, alerts_page_tab):
    alerts_page_tab.navigate()


@pytest.fixture()
def setup_for_iframe_tab(chromedriver, iframe_tab):
    iframe_tab.navigate()


@pytest.fixture()
def setup_for_nested_iframe_tab(chromedriver, nested_iframe_tab):
    nested_iframe_tab.navigate()

# widgets tub setup


@pytest.fixture()
def setup_for_accordian_tab(chromedriver, accordian_tab):
    accordian_tab.navigate()


@pytest.fixture()
def setup_for_auto_complete_tab(chromedriver, auto_complete_tab):
    auto_complete_tab.navigate()


@pytest.fixture()
def setup_for_date_picker_tab(headed_chromedriver, date_picker_tab):
    date_picker_tab.navigate()


@pytest.fixture()
def setup_for_menu_tab(chromedriver, menu_tab):
    menu_tab.navigate()


@pytest.fixture()
def setup_for_progress_bar_tab(chromedriver, progress_bar_tab):
    progress_bar_tab.navigate()


@pytest.fixture()
def setup_for_select_menu_tab(chromedriver, select_menu_tab):
    select_menu_tab.navigate()


@pytest.fixture()
def setup_for_slider_tab(chromedriver, slider_tab):
    slider_tab.navigate()


@pytest.fixture()
def setup_for_tabs_page(chromedriver, tabs_page):
    tabs_page.navigate()


@pytest.fixture()
def setup_for_tool_tips_tab(chromedriver, tool_tips_tab):
    tool_tips_tab.navigate()

# interactions page setups


@pytest.fixture()
def setup_for_sortable_tab(chromedriver, sortable_tab):
    sortable_tab.navigate()


@pytest.fixture()
def setup_for_selectable_tab(chromedriver, selectable_tab):
    selectable_tab.navigate()


@pytest.fixture()
def setup_for_resizable_tab(chromedriver, resizable_tab):
    resizable_tab.navigate()


@pytest.fixture()
def setup_for_droppable_tab(headed_chromedriver, droppable_tab):
    droppable_tab.navigate()


@pytest.fixture()
def setup_for_dragabble_tab(chromedriver, dragabble_tab):
    dragabble_tab.navigate()

# book store setup


@pytest.fixture()
def setup_for_book_store_page(headed_chromedriver, login_and_register_tab, profile_tab, book_store_tab):
    login_and_register_tab.navigate()
    login_and_register_tab.create_user_and_login_to_account()
    profile_tab.go_to_bookstore()
    book_store_tab.add_books_to_collection()
    profile_tab.manipulate_books_in_profile()

# webdriver quit


@pytest.fixture()
def chromedriver_quit(chromedriver):
    yield chromedriver
    chromedriver.quit()


@pytest.fixture()
def chromedriver_quit(headed_chromedriver):
    yield headed_chromedriver
    headed_chromedriver.quit()
