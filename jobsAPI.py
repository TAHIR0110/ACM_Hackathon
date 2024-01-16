import os
from serpapi import GoogleSearch

inp_job = "java"

params = {
  "api_key": "74667d45acf8d73e71f442fcea119219a9c88b09bb187292159a3fc88235289c",
  "engine": "google_jobs",
  "google_domain": "google.com",
  "q": str(inp_job)
}

search = GoogleSearch(params)
result = search.get_dict()


Job_ID = []
for job_result in result['jobs_results']:
    Job_ID.append((job_result['job_id'],job_result['company_name'],job_result['title']))
print('1---------------------------------------------------------------1')

for job_id in Job_ID:
    params = {
        "api_key": "74667d45acf8d73e71f442fcea119219a9c88b09bb187292159a3fc88235289c",
        "engine": "google_jobs_listing",
        "q": str(job_id[0])
  }
    search = GoogleSearch(params)
    results = search.get_dict()
    try:
      print('---------------------------------------------------------------')
      print(job_id[1])
      print(job_id[2])
      print(results['apply_options'])
    except:
       continue
    