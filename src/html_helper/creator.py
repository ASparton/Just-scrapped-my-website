from bs4 import BeautifulSoup, PageElement

def create_project_card(html: BeautifulSoup, project_infos: dict) -> PageElement:
    """Create a piece of html to present the project infos"""
    
    p_container_tag = html.new_tag('li')
    title_tag = html.new_tag('h1')
    category_tag = html.new_tag('h4')
    skills_container_tag = html.new_tag('ul')
    description_tag = html.new_tag('p')
    
    title_tag.string = project_infos['title']
    category_tag.string = project_infos['category']
    for skill in project_infos['skills']:
        skill_tag = html.new_tag('li')
        skill_tag.string = skill
        skills_container_tag.append(skill_tag)
    description_tag.string = project_infos['description']
    
    p_container_tag.append(title_tag)
    p_container_tag.append(category_tag)
    p_container_tag.append(skills_container_tag)
    p_container_tag.append(description_tag)
    return p_container_tag