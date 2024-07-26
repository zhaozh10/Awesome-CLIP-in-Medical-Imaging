import os
import csv
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

SCRAPERAPI_KEY = '11c67af25de7d438fab8a02338f7330b'

import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

import requests
from bs4 import BeautifulSoup
import urllib.parse


def get_article_info(article_name):
    # 使用 ScraperAPI 代理
    search_url = f'https://scholar.google.com/scholar?q={urllib.parse.quote(article_name)}'
    proxy_url = f'http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={search_url}'
    
    search_response = requests.get(proxy_url)
    if search_response.status_code != 200:
        raise Exception(f"Failed to retrieve search page: {search_response.status_code}")
    
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    
    try:
        # 查找第一个搜索结果
        first_result = search_soup.find('div', class_='gs_ri')
        if not first_result:
            print(f"Title '{article_name}' not found")
            return "Reject", "Reject"
        
        # 查找文章链接
        article_link_tag = first_result.find('h3', class_='gs_rt').find('a')
        if not article_link_tag:
            print(f"Title '{article_name}' has no article link")
            return "Reject", "Reject"
        
        article_link = article_link_tag['href']
        
        # 检查链接是否是绝对链接
        if not article_link.startswith('http'):
            article_link = urllib.parse.urljoin(search_url, article_link)
        
        # 使用 ScraperAPI 代理获取文章页面
        article_proxy_url = f'http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={article_link}'
        article_response = requests.get(article_proxy_url)
        if article_response.status_code != 200:
            raise Exception(f"Failed to retrieve article page: {article_response.status_code}")
        
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        
        # 提取作者信息
        authors_tag = article_soup.find('div', id='authors')
        if authors_tag:
            authors = authors_tag.text.strip().split(';')[0]
            print(f"Authors: {authors}")
        # 尝试从其他HTML结构中提取作者信息
        else:
            authors = []
            author_links = article_soup.find_all('a', href=True)
            for link in author_links:
                if "searchtype=author" in link['href']:
                    authors.append(link.text)
            if authors:
                authors = ', '.join(authors)
                print(f"Authors from alternate structure: {authors}")
            
        
        # 提取 PDF 链接
        pdf_link = None
        links = article_soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and ('pdf' or 'View PDF' ) in href:
                pdf_link = urllib.parse.urljoin(article_link, href)
                print(f"PDF Link: {pdf_link}")
                break
        
        if not pdf_link:
            # 重新搜索并提取信息
            search_response = requests.get(proxy_url)
            if search_response.status_code != 200:
                raise Exception(f"Failed to retrieve search page again: {search_response.status_code}")
            
            search_soup = BeautifulSoup(search_response.text, 'html.parser')
            pdf_tag = search_soup.find('div', class_='gs_or_ggsm')
            if pdf_tag:
                pdf_link_tag = pdf_tag.find('a')
                if pdf_link_tag and 'href' in pdf_link_tag.attrs:
                    pdf_link = pdf_link_tag['href']
                    print(f"Updated PDF Link: {pdf_link}")
            
            # 提取作者信息
            authors_tag = search_soup.find('div', class_='gs_fmaa')
            if authors_tag:
                authors = ', '.join([a.text for a in authors_tag.find_all('a')])
                print(f"Updated Authors: {authors}")
            else:
                authors = "Reject"
        
        return authors, pdf_link
    
    except Exception as e:
        print(f"Error parsing the search results for '{article_name}': {e}")
        return "Reject", "Reject"


def process_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        if line.strip():
            # 在第一个 \ 后面添加回车
            line = re.sub(r'\\ ', '\\\n', line, count=1)
            # 在第二个 \ 后面添加回车
            line = re.sub(r'\\ ', '\\\n', line, count=1)
            # 在行末添加回车和空行
            line = line.rstrip() + '\n\n'
            processed_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)


# 定义字典
valid_class = {
    "Classification": "Classification",
    "Dense Prediction": "Dense_Prediction"
}


# 初始化变量
ignore_info = []
cross_modal = []
dense_prediction = []
classification = []
cross_modal_ar = []
dense_prediction_ar = []
classification_ar = []

# 读取CSV文件
with open('./Downstream01.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year'].startswith('2024'):
            area = row['HyperCLass']
            # 检查HyperCLass是否在有效集合中
            matched = False
            for key in valid_class.keys():
                if area.startswith(key):
                    matched = True
                    new_area = valid_class[key]
                    PaperName = row['\ufeffName']
                    Publications = row['Publications']
                    
                    authors,paper_link = get_article_info(PaperName)
                    info = f"[**{Publications} 2024**] {PaperName} \\ _{authors}_ \\ [[paper]({paper_link})]"
                    
                    if Publications.lower() == 'arxiv':
                        if new_area == 'Cross_modal':
                            cross_modal_ar.append(info)
                        elif new_area == 'Dense_Prediction':
                            dense_prediction_ar.append(info)
                        else:
                            classification_ar.append(info)
                    else:
                        if new_area == 'Cross_modal':
                            cross_modal.append(info)
                        elif new_area == 'Dense_Prediction':
                            dense_prediction.append(info)
                        else:
                            classification.append(info)
                    break
            
            if not matched:
                ignore_info.append(row)

# 将ignore_info写入
with open('DownstreamIgnore.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(ignore_info)

# 合并arxiv和非arxiv列表
cross_modal.extend(cross_modal_ar)
dense_prediction.extend(dense_prediction_ar)
classification.extend(classification_ar)
print("...")
# 将列表内容写入preTraining00.txt文件
with open('./downstream.txt', 'w', encoding='utf-8') as txtfile:
    def write_section(title, content):
        txtfile.write(f"# {title}\n\n")
        txtfile.write("\n".join(content))
        txtfile.write("\n\n")
    
    write_section("**Cross_modal**", cross_modal)
    write_section("**Dense_Prediction**", dense_prediction)
    write_section("**Classification**", classification)

input_file = 'downstream.txt'
output_file = 'new.txt'
# 处理文件
process_text_file(input_file, output_file)