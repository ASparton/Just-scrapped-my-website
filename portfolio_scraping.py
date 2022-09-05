from requests import get as get_request
from bs4 import BeautifulSoup

def get_html_at_url(url: str) -> BeautifulSoup:
    """Return a BS4 instance representing the html of the page at the given url, or None if an error occurred."""
    
    # Request html
    response = get_request(url, allow_redirects=False)
    
    # Check error
    if (response.status_code != 200):
        return None
    
    # Otherwise return the html
    return BeautifulSoup(response.text, features='html5lib')

def get_project_title(html: BeautifulSoup) -> str:
    """Search for the project title of the page and returns it if found, otherwise returns None."""
    return html.find(name='h1').string

def get_project_category(html: BeautifulSoup) -> str:
    """Search for the project category of the page and returns it if found, otherwise returns None."""
    return html.find(class_='projectOverview_catAndYearContainer__UBxNF').find(name='p').string

def get_project_skills(html: BeautifulSoup) -> list[str]:
    """Search for the project skills of the page and returns them if found, otherwise returns an empty array."""
    skills = []
    
    skills_list = html.find(name='ul', class_='projectOverview_skillsContainer__G1VUG')
    for skill in skills_list.find_all(name='li'):
        skills.append(skill.find(name='p').string)
    
    return skills

def get_project_infos(html: BeautifulSoup) -> dict:
    """Build a dictionnary containing the project infos (title, category, skills)."""
    
    project_infos = {}
    project_infos['title'] = get_project_title(html)
    project_infos['category'] = get_project_category(html)
    project_infos['skills'] = get_project_skills(html)
    return project_infos

# Get html of page to scrap
projects_infos = []

for i in range(1, 10):
    html = get_html_at_url(f'https://www.asparton.com/projects/{i}')
    if html != None:
        projects_infos.append(get_project_infos(html))
    
print('---- BY CATEGORIES -----')
projects_infos.sort(key=lambda project: project['category'])
for project in projects_infos:
    print(project)
    
print('\n\n---- BY TITLE -----')
projects_infos.sort(key=lambda project: project['title'])
for project in projects_infos:
    print(project)
    
print('\n\n---- BY NUMBER OF SKILLS -----')
projects_infos.sort(key=lambda project: len(project['skills']))
for project in projects_infos:
    print(project)