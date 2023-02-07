import time

from playwright.sync_api import expect
from Pages.MainPage import MainPage
from Pages.ClickPage import ClickPage
from Pages.DoubleClickPage import DoubleClickPage
from Pages.TextInput import TextInput
from Pages.ProgressBar import ProgressBar
from Pages.DynamicTable import DynamicTable
from Pages.SampleApp import SampleApp
from Pages.nbsp import nbsp
from Pages.Ajax import Ajax
from Pages.OverlappedElement import OverlappedElement
from Pages.Visibility import Visibility
from Pages.VerifyText import VerifyText
from Pages.Dynamic_ID import Dynamic_ID


def test_click(page):
    main_page = MainPage(page)
    click_page = ClickPage(page)
    main_page.load()
    main_page.click_click()
    click_page.click_button()
    expect(click_page.click_page_link).to_have_class('btn btn-success')


def test_double_click(page):
    main_page = MainPage(page)
    double_click_page = DoubleClickPage(page)
    main_page.load()
    main_page.click_double_click()
    double_click_page.double_click()


def test_input(page):
    main_page = MainPage(page)
    text_input = TextInput(page)
    main_page.load()
    main_page.click_input_text()
    time.sleep(2)
    text_input.input_text('SALUT')
    time.sleep(2)
    text_input.click_new_button()
    expect(page.locator('id=updatingButton')).to_have_text('SALUT')


def test_progress(page):
    main_page = MainPage(page)
    progress_bar = ProgressBar(page)
    main_page.load()
    main_page.click_progress_bar()
    progress_bar.start()
    progress_bar.stop()


def test_dynamic_table(page):
    main_page = MainPage(page)
    dynamic_table = DynamicTable(page)
    main_page.load()
    main_page.click_dynamic_table()
    time.sleep(2)
    assert dynamic_table.compare() is True


def test_sample_app(page):
    main_page = MainPage(page)
    sample_app = SampleApp(page)
    main_page.load()
    main_page.click_sample_app()
    time.sleep(2)
    sample_app.enter_username('Mihai')
    sample_app.enter_password('pwd')
    sample_app.click_login()
    time.sleep(1)
    assert sample_app.success_logged_in() == True


def test_nbsp(page):
    main_page = MainPage(page)
    nbsp_page = nbsp(page)
    main_page.load()
    main_page.click_nbsp()
    time.sleep(1)
    nbsp_page.click_button()
    time.sleep(1)


def test_ajax(page):
    main_page = MainPage(page)
    ajax_page = Ajax(page)
    main_page.load()
    main_page.click_ajax()
    assert ajax_page.element_appear() == True


def test_overlapped(page):
    main_page=MainPage(page)
    overlapped_page = OverlappedElement(page)
    main_page.load()
    main_page.click_overlapped_page()
    overlapped_page.complete_field('1', 'Mihai')


def test_visibility(page):
    main_page = MainPage(page)
    visibility_page = Visibility(page)
    main_page.load()
    main_page.click_visibility()
    visibility_page.hit_hide_button()
    time.sleep(1)
    assert visibility_page.removed_button.is_visible() is True
    assert visibility_page.zero_width_button.is_visible() is True
    assert visibility_page.overlapped_button.is_visible() is True
    assert visibility_page.transparent_button.is_visible() is True
    assert visibility_page.visibility_hidden.is_visible() is True
    assert visibility_page.display_none.is_visible() is True
    assert visibility_page.off_screen.is_visible() is True


def test_verify_text(page):
    main_page = MainPage(page)
    verify_text = VerifyText(page)
    main_page.load()
    main_page.click_verify_text()
    assert verify_text.return_text() is True


def test_dynamic_ID(page):
    main_page = MainPage(page)
    dynamic_id = Dynamic_ID(page)
    main_page.load()
    main_page.click_dynamic_id()
    time.sleep(1)
    dynamic_id.click_button()
    time.sleep(1)
    assert dynamic_id.button.is_visible() is True
