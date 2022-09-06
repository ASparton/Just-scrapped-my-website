from bs4 import BeautifulSoup

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

def get_project_description(html: BeautifulSoup) -> str:
    """Search for the project description in the given html

    Args:
        html (BeautifulSoup): All the html content of the page

    Returns:
        str: The project's description
    """
    
    return html.find(name='p', class_='projectOverview_description__b4tHL').string