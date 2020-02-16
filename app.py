import pdfkit
import html_creator
import sys
#import listing_data


def create_resume(company):
    #company = listing_data.Check_listing().request_data(url)
    html_creator.Resume().compose_resu(company)
    pdfkit.from_file('resume_new.html', 'resume_'+company+'.pdf')


def create_universal():
    html_creator.Resume().compose_un()
    pdfkit.from_file('resume_new.html', 'resume_John_Doe.pdf')


try:
    create_resume(sys.argv[1])
except:
    create_universal()
