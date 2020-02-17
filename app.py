''' easy composing of resume, includes company name to the cv and converts to pdf'''
import sys
import pdfkit
import html_creator
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
    company = listing_data.Checklisting().request_data(url)
    return create_resume(company)


try:
    SYS_ARGS = sys.argv[1]
    if sys_args.startswith('https'):
        create_from_li(SYS_ARGS)
    else:
        create_resume(SYS_ARGS)
except:
    create_universal()
