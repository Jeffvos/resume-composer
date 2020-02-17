""" Preparing the html version """
import bs4


class Resume():
    ''' creation of html resume to later conver to pdf '''

    def __init__(self):
        with open("resume.html") as resu:
            content = resu.read()
            soup = bs4.BeautifulSoup(content)
            self._soup = soup

    def compose_resu(self, company):
        ''' compose the resume'''
        company_line = "Eager to join {}".format(company)
        company_goal = "."
        self._soup.find(id="company").replace_with(company_line)
        self._soup.find(id="company_goal").replace_with(company_goal)
        return self._write_out()

    def compose_un(self):
        ''' composes universal (no company name) resume '''
        return self._write_out()

    def _write_out(self):
        ''' write out to a new html file resume_new.html '''
        with open("resume_new.html", "w") as output_resu:
            output_resu.write(str(self._soup))
