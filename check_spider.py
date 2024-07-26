import os
import requests
from bs4 import BeautifulSoup

SCRAPERAPI_KEY = '11c67af25de7d438fab8a02338f7330b'

def get_article_info(article_name):
    # 使用 ScraperAPI 代理
    search_url = f'https://scholar.google.com/scholar?q={article_name}'
    proxy_url = f'http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={search_url}'
    
    search_response = requests.get(proxy_url)
    if search_response.status_code != 200:
        raise Exception(f"Failed to retrieve data: {search_response.status_code}")
    
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    
    try:
        first_result = search_soup.find('div', class_='gs_ri')
        if not first_result:
            raise Exception("No results found")
        
        article_link_tag = first_result.find('h3', class_='gs_rt').find('a')
        if not article_link_tag:
            raise Exception("No article link found")
        
        article_link = article_link_tag['href']
        article_proxy_url = f'http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={article_link}'
        
        article_response = requests.get(article_proxy_url)
        if article_response.status_code != 200:
            raise Exception(f"Failed to retrieve article data: {article_response.status_code}")
        
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        
        # 提取作者信息
        authors_tag = article_soup.find('div', id='authors')
        if authors_tag:
            authors = authors_tag.text.strip()
        else:
            authors = "Unknown"
        
        # 提取 PDF 链接
        pdf_link = None
        links = article_soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and 'pdf' in href:
                pdf_link = os.path.join(os.path.dirname(article_link), href)
                break
        
        if not pdf_link:
            pdf_link = "No PDF link available"
        
        return authors, pdf_link
    
    except Exception as e:
        raise Exception(f"Error parsing the search results: {e}")

# 测试函数
article_name = "Deep Residual Learning for Image Recognition"
authors, pdf_link = get_article_info(article_name)
print(f"Authors: {authors}")
print(f"PDF Link: {pdf_link}")
