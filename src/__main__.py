from requests import get as get_request
from bs4 import BeautifulSoup

from scraping import scraping
from html_helper import creator

def get_html_at_url(url: str) -> BeautifulSoup:
    """Return a BS4 instance representing the html of the page at the given url, or None if an error occurred."""
    
    # Request html
    response = get_request(url, allow_redirects=False)
    
    # Check error
    if (response.status_code != 200):
        return None
    
    # Otherwise return the html
    return BeautifulSoup(response.text, features='html5lib')

def get_project_infos(html: BeautifulSoup) -> dict:
    """Build a dictionnary containing the project infos (title, category, skills)."""
    
    project_infos = {}
    project_infos['title'] = scraping.get_project_title(html)
    project_infos['category'] = scraping.get_project_category(html)
    project_infos['skills'] = scraping.get_project_skills(html)
    project_infos['description'] = scraping.get_project_description(html)
    return project_infos


# Get projects infos from website
projects_infos = []
for i in range(1, 10):
    html = get_html_at_url(f'https://www.asparton.com/projects/{i}')
    if html != None:
        projects_infos.append(get_project_infos(html))
    
# Put the retrieved data into a new html page
with open('./input.html', 'r') as result_file:
    result_html = BeautifulSoup(result_file, features='html5lib')
    
p_list = result_html.find(id='projects-list')
for project_infos in projects_infos:
    p_list.append(creator.create_project_card(result_html, project_infos))
    
# Write changes done in doc
with open('./output.html', 'w') as result_file:
    result_file.write(result_html.prettify())