import pdfkit
import html_creator
import sys
import listing_data


def create_resume(company):
    ''' create with company name '''
    html_creator.Resume().compose_resu(company)
    pdfkit.from_file('resume_new.html', 'resume_'+company+'.pdf')


def create_universal():
    ''' no company name '''
    html_creator.Resume().compose_un()
    pdfkit.from_file('resume_new.html', 'resume_John_Doe.pdf')


def create_from_li(url):
    ''' use for linkedin listings '''
    company = listing_data.Check_listing().request_data(url)
    return create_resume(company)


try:
    sys_args = sys.argv[1]
    if sys_args.startswith('https'):
        create_from_li(sys_args)
    else:
        create_resume(sys_args)
except:
    create_universal()
