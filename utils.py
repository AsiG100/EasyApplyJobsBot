import string
import math
import constants

def jobsToPages(numOfJobs: string) -> int:
  print(numOfJobs)
  number_of_pages = 1
  
  if (' ' in numOfJobs):
    spaceIndex = numOfJobs.index(' ')
    print(spaceIndex)
    totalJobs = (numOfJobs[0:spaceIndex])
    totalJobs_int = int(totalJobs.replace(',', ''))
    number_of_pages = math.ceil(totalJobs_int/constants.jobs_per_page)
    if (number_of_pages > 40 ): number_of_pages = 40

  else:
      number_of_pages = int(numOfJobs)

  return number_of_pages

