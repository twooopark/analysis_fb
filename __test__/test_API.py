from analysis_fb.collect.api import api

# params = {'since':20170101, 'until':20171231, 'limit':50}
# url = api.fb_gen_url(node='jtbcnews', a=10, b=20)
#  print(url)

# id = api.fb_name_to_id('jtbcnews')
# print(id)

posts = api.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-12-31')
print(posts)
print(len(posts))