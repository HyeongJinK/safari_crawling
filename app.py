from selenium import webdriver

user = "wkzkfmxk23@gmail.com"
password = "wnrdmffo12!"

browser = webdriver.PhantomJS()
browser.implicitly_wait(2)

def login(user, password):
    url_login = "https://learning.oreilly.com/accounts/login/"
    browser.get(url_login)

    browser.find_element_by_id("id_email").send_keys(user)
    browser.find_element_by_id("id_password1").send_keys(password)

    form = browser.find_element_by_css_selector("input#login[type=submit]")
    form.submit()

def get_book_link_listBysearch_page(search, page):
    url_list = "https://learning.oreilly.com/search/?query={search}&extended_publisher_data=true&highlight=true&include_assessments=false&include_case_studies=true&include_courses=true&include_orioles=true&include_playlists=true&is_academic_institution_account=false&formats=book&sort=date_added&page={page}"
    browser.get(url_list.format(search=search, page=page))
    result = []
    cards = browser.find_elements_by_css_selector("article.column--2iymX h4 a")
    for card in cards:
        result.append(card.get_attribute('href'))

    return result

def book_table_contents(href):
    browser.get(href)
    result = []
    table_contents = browser.find_elements_by_css_selector("ol.detail-toc li > a")
    for tc in table_contents:
        li = tc.get_attribute("href").split("#")[0]
        #if result.find(li) != 0:
            result.append(li)
    
    return result




login(user, password)

book_link_list = get_book_link_listBysearch_page("", 0)

for link in book_link_list:
    table_link = book_table_contents(link)
    for tl in table_link:
        print(tl)
