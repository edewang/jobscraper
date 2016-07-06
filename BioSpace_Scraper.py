
# coding: utf-8

# In[8]:

import urllib.request
from bs4 import BeautifulSoup
import re
f = open('joblist.txt', 'w')


# In[9]:

url = "http://www.biospace.com/jobs/job-search-query/?PositionTypeList=FULL+TIME&Location=CA&Radius=50&State=California&Country=United+States&PageSize=10&PageIndex=1"

def job_grabber(url, start=1):
    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    jobs = soup.find_all(id="spnDatePosted")
    date = jobs[0].get_text(strip=True)
    done = False
    for job in jobs:
        if job.get_text(strip=True) == date:
            job_title = job.find_next_sibling()
            job_employer = job_title.find_next_sibling()
            job_location = job_employer.find_next_sibling()
            job_desc = job_location.find_next_sibling().find_next_sibling()
            print(str(start) + ". " + str(job_title.a))
            f.write(str(start) + ". " + str(job_title.a))
            print(job_employer.get_text(strip=True) + "\t" + re.sub('\s{2,}', '', job_location.get_text(strip=True)))
            f.write(job_employer.get_text(strip=True) + "\t" + re.sub('\s{2,}', '', job_location.get_text(strip=True)))
            print(re.sub('\n\n', '\n', job_desc.get_text(strip=True)) + "\n")
            f.write(re.sub('\n\n', '\n', job_desc.get_text(strip=True)) + "\n")
            start += 1
        else:
            done = True
            break
    if not done:
        job_grabber(url[:-1] + str(int(url[-1])+1), start)

job_grabber(url)


# In[ ]:



