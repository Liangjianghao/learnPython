url='http://www.btrabbit.cc/search/%s.html'%name
print url	
response=requests.get(url).content
selector = html.fromstring(response)
hrefs=selector.xpath('//div[@class="search-item detail-width"]')

selector = html.fromstring(driver.page_source)
# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
hrefs=selector.xpath('//table/tbody/tr')